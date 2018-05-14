import sys

#地图(从文件中获取的二维数组)
maze=[]
#起点
start=None
#终点
end=None
#开放列表（也就是有待探查的地点）
open_list={}
#关闭列表  (已经探查过的地点和不可行走的地点)
close_list={}
#地图边界(二维数组的大小，用于判断一个节点的相邻节点是否超出范围)
map_border=()
#方向
orientation=[]

class Node(object):
    def __init__(self,father,x,y):
        if x<0 or x>=map_border[0] or y<0 or y>=map_border[1]:
            raise Exception('坐标错误')

        self.father=father
        self.x=x
        self.y=y

        if father !=None:
            self.G=father.G+1
            self.H=distance(self,end)
            self.F=self.G+self.H
        else:
            self.G=0
            self.H=0
            self.F=0

    def reset_father(self,father,new_G):
        if father!=None:
            self.G=new_G
            self.F=self.G+self.H

        self.father=father

#计算距离
def distance(cur,end):
    return abs(cur.x-end.x)+abs(cur.y-end.y)
        

#在open_list中找到最小F值的节点
def min_F_node():
    global open_list
    if len(open_list)==0:
        raise Exception('路径不存在')

    _min=9999999999999999
    _k=(start.x,start.y)

    #以列表的形式遍历open_list字典
    for k,v in open_list.items():
        if _min>v.F:
            _min=v.F
            _k=k

    return open_list[_k]

#把相邻的节点加入到open_list之中，如果发现终点说明找到终点
def addAdjacentIntoOpen(node):
    global open_list,close_list
    
    #首先将该节点从开放列表移动到关闭列表之中
    open_list.pop((node.x,node.y))
    close_list[(node.x,node.y)]=node
    adjacent=[]

    #添加相邻节点的时候要注意边界
    #上
    try:
        adjacent.append(Node(node,node.x,node.y-1))
    except Exception as err:
        pass
    #下
    try:
        adjacent.append(Node(node,node.x,node.y+1))
    except Exception as err:
        pass
    #左
    try:
        adjacent.append(Node(node,node.x-1,node.y))
    except Exception as err:
        pass
    #右
    try:
        adjacent.append(Node(node,node.x+1,node.y))
    except Exception as err:
        pass

    #检查每一个相邻的点
    for a in adjacent:
        #如果是终点，结束
        if (a.x,a.y)==(end.x,end.y):
            new_G=node.G+1
            end.reset_father(node,new_G)
            return True
        #如果在close_list中,不去理他
        if (a.x,a.y) in close_list:
            continue
        #如果不在open_list中，则添加进去
        if (a.x,a.y) not in open_list:
            open_list[(a.x,a.y)]=a
        #如果存在在open_list中，通过G值判断这个点是否更近 
        else:
            exist_node=open_list[(a.x,a.y)]
            new_G=node.G+1
            if new_G<exist_node.G:
                exist_node.reset_father(node,new_G)

    return False

#查找路线
def find_the_path(start,end):
    global open_list
    open_list[(start.x,start.y)]=start

    the_node=start
    try:
        while not addAdjacentIntoOpen(the_node):
            the_node=min_F_node()

    except Exception as err:
        #路径找不到
        print(err)
        return False
    return True

#读取文件，将文件中的信息加载到地图(maze)信息中
def readfile(url):
    global maze,map_border
    f=open(url)
    line=f.readline()
    map_size=line.split()
    map_size=list(map(int,map_size))
    x=map_size[0]
    y=map_size[1]
    map_border=(x,y)
    
    i=0
    while line:
        line=f.readline()
        maze.append(list(map(int,line.split())))
        i=i+1
        if i>x-1:
            break


#通过递归的方式根据每个点的父节点将路径连起来
def mark_path(node):
    global orientation
    if node.father==None:     
        return
    
    #print('({x},{y})'.format(x=node.x,y=node.y))
    #将方向信息存储到方向列表中
    if node.father.x-node.x>0:
        orientation.append('L')
    elif node.father.x-node.x<0:
        orientation.append('R')
    elif node.father.y-node.y>0:
        orientation.append('U')
    elif node.father.y-node.y<0:
        orientation.append('D')
    mark_path(node.father)
    
#解析地图,把不可走的点直接放到close_list中
def preset_map():
    global start,end,map_bloder,maze
    row_index=0
    for row in maze:
        col_index=0
        for n in row:
            if n==1:
                block_node=Node(None,col_index,row_index)
                close_list[(block_node.x,block_node.y)]=block_node
            col_index=col_index+1
        row_index=row_index+1
    
if __name__=='__main__':
    #判断在控制台输入的参数时候达到要求
    if len(sys.argv)<6:
        raise Exception('参数格式：文件名 x1 y1 x2 y2   其中x1 y1代表开始坐标，x2 y2代表目标坐标')
    else:
        #从控制台读取参数
        readfile(sys.argv[1])
        start_x=int(sys.argv[2])
        start_y=int(sys.argv[3])
        end_x=int(sys.argv[4])
        end_y=int(sys.argv[5])
        start=Node(None,start_x,start_y)
        end=Node(None,end_x,end_y)

        
        
        preset_map()

        #判断起点终点是否符合要求
        if (start.x,start.y) in close_list or (end.x,end.y) in close_list:
            raise Exception('输入的坐标不可走')

        if find_the_path(start,end):
            mark_path(end)

        #列表方向调整为起点开始
        orientation.reverse()
        str_ori=''
        for o in orientation:
            str_ori=str_ori+o+' '
        print(str_ori)
