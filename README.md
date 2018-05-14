# astar
![](https://ask.qcloudimg.com/draft/1903186/87mc9t9um2.png)

**【警告】 本文章并非面向零基础的人，而是面对黄金段位的LOL大神。本文同样适合出门在外没有导航，就找不到家的孩子。**

在英雄联盟之中，当你和你的队友都苦苦修炼到十八级的时候，仍然与敌方阵营不分胜负，就在你刚买好装备已经神装的时候，你看见信息框中一条队友的消息：“大龙集合”，这个时候你鼠标移到大龙处，轻点右键，然后你就像一个吃瓜群众一样盯着你的英雄，看他走进野区小路，因为你买了日炎斗篷，路过三狼的时候三狼还追着你咬了几口，你的英雄也没有去理会，三狼可算是出了一口气，牛逼坏了！然后你还顺路采了几个蘑菇，因烫到了蓝buff被蓝buff追杀。就连河道里的河蟹都想咬你一口为你在三级的时候杀了它的爷爷而报仇。然而你还是在临死前来到大龙面前，你还没动大龙一根汗毛，就被大龙一个甩尾干趴下了，这时候你旁边的妹纸还很疑惑，你得显示器怎么突然坏掉了，变成黑白的了。

![](https://ask.qcloudimg.com/draft/1903186/gu057t4j62.png)

 那么问题来了，为什么野区套路那么深，而你的英雄不选择走大路沿河道到大龙呢？因为你每确定一个目标，你的英雄就会沿着最短的路线前往。那么你的英雄是怎么找到最近的路线呢？如果你觉的很简单，你自己也能找到，你有你的英雄找的快吗？当你确定目标的时候你的英雄可不是东张西望让后才开始走，更不会走一半发现不对劲有自己回去重头再来。你也许开始对这个问题感兴趣了，那些游戏中的英雄人物是怎么做到的？如果你不玩游戏，那么你肯定用过导航软件，你应该会好奇它是怎么做到的。你能读到这篇文章，那么你一定会写代码，你能用代码去实现这个功能吗？其实我一直都很好奇这个是怎么做到的，我最多也就会写一些增删改查的常规操作。直到我接到了一个实现A-star算法的作业，才弄明白。

## A-star算法

我们假设某个人要从A点到达B点，而一堵墙把这两个点隔开了，如下图所示，绿色 部分代表起点A，红色部分代表终点B，蓝色方块部分代表之间的墙。

![](https://ask.qcloudimg.com/draft/1903186/biw7vpmw7u.png)

你首先会注意到我们把这一块搜索区域分成了一个一个的方格，如此这般，使搜索  区域简单化，正是寻找路径的第一步。这种方法将我们的搜索区域简化成了一个普  通的二维数组。数组中的每一个元素表示对应的一个方格，该方格的状态被标记为  可通过的和不可通过的。通过找出从A点到B点所经过的方格，就能得到AB之间的  路径。当路径找出来以后，这个人就可以从一个格子中央移动到另一个格子中央， 直到抵达目的地。  这些格子的中点叫做节点。当你在其他地方看到有关寻找路径的东西时，你会经常发现人们在讨论节点。为什么不直接把它们称作方格呢？因为你不一定要把你的搜  索区域分隔成方块，矩形、六边形或者其他任何形状都可以。况且节点还有可能位  于这些形状内的任何一处呢？在中间、靠着边，或者什么的。我们就用这种设定， 因为毕竟这是最简单的情况。

当我们把搜索区域简化成一些很容易操作的节点后，下一步就要构造一个搜索来寻 找最短路径。在A\*算法中，我们从A点开始，依次检查它的相邻节点，然后照此继 续并向外扩展直到找到目的地。 我们通过以下方法来开始搜索：

1. 从A点开始，将A点加入一个专门存放待检验的方格的“开放列表”中。这个开放列表 有点像一张购物清单。当前这个列表中只有一个元素，但一会儿将会有更多。列表 中包含的方格可能会是你要途经的方格，也可能不是。总之，这是一个包含待检验 方格的列表。

2.检查起点A相邻的所有可达的或者可通过的方格，不用管墙啊，水啊，或者其他什 么无效地形，把它们也都加到开放列表中。对于每一个相邻方格，将点A保存为它 们的“父方格”。当我们要回溯路径的时候，父方格是一个很重要的元素。稍后我们 将详细解释它。

3.从开放列表中去掉方格A，并把A加入到一个“封闭列表”中。封闭列表存放的是你现 在不用再去考虑的方格。

此时你将得到如下图所示的样子。在这张图中，中间深绿色的方格是你的起始方格， 所有相邻方格目前都在开放列表中，并且以亮绿色描边。每个相邻方格有一个灰色 的指针指向它们的父方格，即起始方格

![](https://ask.qcloudimg.com/draft/1903186/d7ihgvdb1z.png)

接下来，我们在开放列表中选一个相邻方格并再重复几次如前所述的过程。但是我 们该选哪一个方格呢？具有最小F值的那个

**路径排序**

**决定哪些方格会形成路径的关键是这个等式：F = G + H**

G＝从起点A沿着已生成的路径到一个给定方格的移动开销

H＝从给定方格到目的方格的估计移动开销。这种方式常叫做试探，有点困惑人吧。  其实之所以叫做试探法是因为这只是一个猜测。在找到路径之前我们实际上并不知  道实际的距离，因为任何东西都有可能出现在半路上（墙啊，水啊什么的）。本文中 给出了一种计算H值的方法，网上还有很多其他文章介绍的不同方法

我们要的路径是通过反复遍历开放列表并选择具有最小F值的方格来生成的。本文稍 后将详细讨论这个过程。我们先进一步看看如何计算那个等式。

如前所述，G是从起点A沿着已生成的路径到一个给定方格的移动开销，在本例中， 我们指定每一个水平或者垂直移动的开销为  10，对角线移动的开销为 14。因为对角 线的实际距离是 2 的平方根（别吓到啦），或者说水平及垂直移动开销的 1.414 倍。  为了简单起见我们用了 10 和 14 这两个值。比例大概对就好，我们还因此避免了平  方根和小数的计算。这倒不是因为我们笨或者说不喜欢数学，而是因为对电脑来说， 计算这样的数字也要快很多。不然的话你会发现寻找路径会非常慢。

我们要沿特定路径计算给定方格的G值，办法就是找出该方格的父方格的G值，并根 据与父方格的相对位置（斜角或非斜角方向）来给这个G值加上 14 或者 10。在本例 中这个方法将随着离起点方格越来越远计算的方格越来越多而用得越来越多。

有很多方法可以用来估计H值。我们用的这个叫做曼哈顿（Manhattan）方法， 即计算通过水平和垂直方向的平移到达目的地所经过的方格数乘以  10 来得到H值。之所 以叫Manhattan方法是因为这就像计算从一个地方移动到另一个地方所经过的城市  街区数一样，而通常你是不能斜着穿过街区的。重要的是，在计算H值时并不考虑  任何障碍物。因为这是对剩余距离的估计值而不是实际值（通常是要保证估计值不大于实际值）。这就是为什么这个方式被叫做试探法的原因了。

G和H相加就得到了F。第一步搜索所得到的结果如下图所示。每个方格里都标出了F、 G和H值。如起点方格右侧的方格标出的，左上角显示的是F值，左下角是G值，右 下角是H值。

![](https://ask.qcloudimg.com/draft/1903186/dda8x959fa.png)

我们来看看这些方格吧。在有字母的方格中，G＝10，这是因为它在水平方向上离 起点只有一个方格远。起点紧挨着的上下左右都具有相同的G值 10。对角线方向的 方块G值都是 14。

H值通过估算到红色目标方格的曼哈顿距离而得出。用这种方法得出的起点右侧方 格到红色方格有 3 个方格远，则该方格H值就是 30。上面那个方格有 4 个方格远（注 意只能水平和垂直移动），H就是 40。你可以大概看看其他方格的H值是怎么计算出 来的。

每一个方格的F值，当然就不过是G和H值之和了。

**继续搜索**

为了继续搜索，我们简单的从开放列表中选择具有最小 F 值的方格，然后对选中的 方格进行如下操作：

4.将其从开放列表中移除，并加到封闭列表中。

5.检验所有的相邻方格，忽略那些不可通过的或者已经在封闭列表里的方格。如果这 个相邻方格不在开放列表中，就把它添加进去。并将当前选定方格设为新添方格的 父方格。

6.如果某个相邻方格已经在开放列表中了（意味着已经探测过，而且已经设置过父方 格――译者），就看看有没有到达那个方格的更好的路径。也就是说，如果从当前选 中方格到那个方格，会不会使那个方格的 G 值更小。如果不能，就不进行任何操作。

 相反的，如果新路径的 G 值更小，就将该相邻方格的父方格重设为当前选中方格。

（在上图中是改变其指针的方向为指向选中方格。最后，重新计算那个相邻方格的 F 和 G 值。如果你看糊涂了，下面会有图解说明。

好啦，咱们来看看具体点的例子。在初始时的 9 个方块中，当开始方格被加到封闭 列表后，开放列表里还剩 8 个方格。在这八个方格当中，位于起点方格右边的那个 方格具有最小的 F 值 40。所以我们选择这个方格作为下一个中心方格。下图中它以 高亮的蓝色表示。

![](https://ask.qcloudimg.com/draft/1903186/mj56u2bedg.png)

首先，我们将选中的方格从开放列表中移除，并加入到封闭列表中（所以用亮蓝色 标记）。然后再检验它的相邻节点。那么在它紧邻的右边的方格都是墙，所以不管它 们。左边挨着的是起始方格，而起始方格已经在封闭列表中了，所以我们也不管它。

其他四个方格已经在开放列表中，那么我们就要检验一下如果路径经由当前选中方 格到那些方格的话会不会更好，当然，是用 G  值作为参考。来看看选中方格右上角 的那一个方格，它当前的 G 值是 14，如果我们经由当前节点再到达那个方格的话， G 值会是  20（到当前方格的 G 值是 10，然后向上移动一格就再加上 10）。为 20 的 G 值比 14  大，因此这样的路径不会更好。你看看图就会容易理解些。显然从起始点 沿斜角方向移动到那个方格比先水平移动一格再垂直移动一格更直接。

当我们按如上过程依次检验开放列表中的所有四个方格后，会发现经由当前方格的 话不会形成更好的路径，那我们就保持目前的状况不变。现在我们已经处理了所有 相邻方格，准备到下一个方格吧。

我们再遍历一下开放列表，目前只有 7 个方格了。我们挑个 F 值最小的吧。有趣的 是，目前这种情况下，有两个 F 值为 54  的方格。那我们怎么选择呢？其实选哪个都 没关系，要考虑到速度的话，选你最近加到开放列表中的那一个会更快些。当离目  的地越来越近的时候越偏向于选最后发现的方格。实际上这个真的没关系（对待这 个的不同造成了两个版本的 A\*算法得到等长的不同路径）。

那我们选下面的那个好了，就是起始方格右边的，下图所示的那个

![](https://ask.qcloudimg.com/draft/1903186/fra65vg3nh.png)

这一次，在我们检验相邻方格的时候发现右边紧挨的那个是墙，就不管它了。上面  挨着的那个也同样忽略。还有右边墙下面那个方格我们也不管。为什么呢？因为你  不可能切穿墙角直接到达那个格子。实际上你得先向下走然后再通过那个方格。这  个过程中是绕着墙角走。（注意：穿过墙角的这个规则是可选的，取决于你的节点是 如何放置的。）

那么还剩下其他五个相邻方格。当前方格的下面那两个还不在开放列表中，那我们  把它们加进去并且把当前方格作为它们的父方格。其他三个中有两个已经在封闭列  表中了（两个已经在图中用亮蓝色标记了，起始方格，上面的方格），所以就不用管  了。最后那个，当前方格左边挨着的，要检查一下经由当前节点到那里会不会降低 它的 G  值。结果不行，所以我们又处理完毕了，然后去检验开放列表中的下一个格 子。

重复这个过程直到我们把目的方格加入到开放列表中了，那时候看起来会像下图这个样子。

![](https://ask.qcloudimg.com/draft/1903186/hwuxef5vm8.png)

注意到没？起始方格下两格的位置，那里的格子已经和前一张图不一样了。之前它 的 G 值是 28 并且指向右上方的那个方格。现在它的 G  值变成了 20 并且指向了正上 方的方格。这个改变是在搜索过程中，它的 G 值被核查时发现在某个新路径下可以  变得更小时发生的。然后它的父方格也被重设并且重新计算了 G 值和 F 值。在本例  中这个改变看起来好像不是很重要，但是在很多种情况下这种改变会使到达目标的 最佳路径变得非常不同。

那么我们怎样来自动得出实际路径的呢?很简单，只要从红色目标方格开始沿着每一  个方格的指针方向移动，依次到达它们的父方格，最终肯定会到达起始方格。那就 是你的路径！如下图所示。从 A 方格到 B  方格的移动就差不多是沿着这个路径从每 个方格中心（节点）移动到另一个方格中心，直到抵达终点。

![](https://ask.qcloudimg.com/draft/1903186/c2g1a2jg8y.png)

**代码示例：**

这是一段python3代码，它会读取一个类似下面地图的文件，其中第一行是地图的大小，其他的地方0代表可行，1代表不可走。为了简单的给出编程思路，这个假设人物只会上下左右移动。命令行参数分别为地图文件、起点坐标x、y终点坐标x、y。

地图文件名：testgrid\_small.txt

```
5    3
0    0    1    0    0
1    0    1    0    0
0    0    0    0    1
```

代码文件名：astar.py

```
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

astar.py
```

运行结果：

​

![](https://ask.qcloudimg.com/draft/1903186/pd3mwx330z.png)

​
