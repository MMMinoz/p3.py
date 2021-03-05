#DrawPython蟒蛇
import turtle as tur
# #设置窗体大小 startx,starty非必需，默认在屏幕中间
# turtle.setup(width,height,startx,starty)
# #海龟到(x,y)坐标
# turtle.goto(x , y)
# #海龟向前移动d
# #当d值为正数时向前移动
# #当d为负数时向后移动
# turtle.fd(d)
# #画笔向后移动d
# turtle.bk(d)
# #r弧形半径
# #当radius值为正数时，圆心在当前位置/小海龟左侧
# #当radius值为负数时，圆心在当前位置/小海龟右侧
# #angle弧形角度 当无该参数或参数为None时，绘制整个圆形
# #当extent值为正数时，顺小海龟当前方向绘制。
# #当extent值为负数时，逆小海龟当前方向绘制。
# turtle.circle(r,angle)
# #改变海龟行进方向，只改变方向并不前进
# #在执行完tur.fd()后，小乌龟恢复到正X方向
# #angle为绝对度数
# turtle.seth(angle)
# #海龟左转/右转angle度
# #angle为海龟度数
# turtle.left(angle)



# tur.setup(650,350)
# #抬笔
# tur.penup()
# tur.fd(-250)
# #落笔
# tur.pendown()
# tur.pensize(25)
# tur.pencolor("pink")
# tur.seth(-40)
# for i in range(4):
#     tur.circle(40,80)
#     tur.circle(-40,80)
# tur.circle(40,80/2)
# tur.fd(40)
# tur.circle(16,180)
# tur.fd(40*2/3)
# tur.done()

# tur.setup(400,400)
# tur.goto(100,100)
# tur.goto(0,-200)
# tur.goto(-100,100)
# tur.goto(0,0)

# tur.seth(45)
# tur.circle(-100,90)
# tur.circle(-200,120)

# tur.colormode(255)
# tur.color("pink")
# tur.left(45)
# tur.fd(150)
# tur.right(135)
# tur.fd(200)
# tur.left(135)
# tur.fd(150)
# tur.done()


# tur.setup(500,500)
# tur.pencolor("purple")
# tur.width(25)
# tur.penup()
# tur.fd(-250)
# tur.pendown()
# tur.seth(-40)
# for i in range(4):
#     tur.circle(40,80)
#     tur.circle(-40,80)
# tur.circle(40,40)
# tur.fd(40)
# tur.circle(16,180)
# tur.fd(40)
# tur.done()


#tur.seth()在执行完tur.fd()后，小乌龟恢复到正X方向
#而tur.left()/tur.right()执行完后方向不恢复

# tur.setup(500,500)
# tur.penup()
# tur.pencolor("black")
# tur.pendown()
# for i in range(4):
#     tur.seth(90*i)
#     tur.fd(150)
#     tur.right(90)
#     tur.circle(-100,45)
#     tur.goto(0,0)
#
# tur.done()


# tur.setup(500,500)
# tur.penup()
# tur.color("yellow")
# tur.fillcolor("red")
# tur.width("5")
# tur.fd(-150)
# tur.pendown()
#
# tur.begin_fill()
# for i in range(5):
#     tur.fd(300)
#     tur.right(144)
# tur.end_fill()
#
# tur.write("五角星",font=('宋体',20,'normal'))
#
# tur.done()

# 椭圆
tur.setup(500,500)
tur.seth(90)
len = 1

for i in range(2):
    for j in range(60):
        if j <30:
            len += 0.2
        else:
            len -=0.2
        tur.fd(len)
        tur.left(3)

tur.done()

#树枝
#利用克隆和递归
# tur.setup(800,800)
# tur.width(5)
# tur.color("green")
#
# tur.goto(0,-200)#起点
# tur.seth(90)
# def branch(plist, len):            # 自定义函数，画树枝
#     if (len > 15):                 # 递归的退出条件
#         list = []                  # 新画笔列表
#         for p in plist:            # 遍历旧画笔列表
#             p.forward(len)
#             q = p.clone()
#             p.left(65)
#             q.right(65)
#             list.append(p)         # 存入新画笔列表
#             list.append(q)         # 存入新画笔列表
#         branch(list, len * 0.65)   # 递归，list为新画笔列表，树枝长65%
#
# branch([tur], 200)
# tur.done()

# 集合 set类 去重
# 列表有序，集合无序
# S = {'P','Y','t','h','O','n'}
# T = {'P','Y','T'',h','o','n'}
# S - T#差
# S | T#并
# S & T#交
# S ^ T#补
# S >= T (S <= T) #判断包含关系
#
# S.add(x)#向S中添加x(如果x不在S中)
# S.remove(x)#若S中有x则删除，没有则报错
# S.discard(x)#若S中有x则删除，没有不报错
# S.clear()#清空
# S.pop()#从集合中随机返回一个元素，并删除，若S为空则返回异常
# S.copy()#返回S的一个副本
# #创建空集合只能由set
# s = set({})
# print(s)
#
# 序列
# 字符串类型 列表类型 元组类型
#
# ls lt指向同一个 只是名字不同
# ls = ['P','Y','t','h','O','n']
# lt = ls
# #在列表中增加一个元素
# ls.append(1234)
# print(ls)
# #在k位置插入一个元素
# ls.insert(3,'python')
# print(ls)
# #倒转
# ls.reverse()
# print(ls)
# #删除ls中某个位置的元素
# del ls[1]
# #删除ls中某切片的元素
# del ls[1:4]
# #返回n的索引
# ls.index(n)
# max(ls)
#
# 映射 字典类型dict
# d = {"中国":"北京","美国":"华盛顿","法国":"纽约"}
# print(d["中国"])
# print(d.keys())
# print(d.values())
# #若key存在，则返回value,否则输出default
# print(d.get("中国","不存在"))
# #若key存在，则取出value,否则输出default
# print(d.pop("中国","不存在"))
# #返回键值对元组
# print(d.items())
# #随机取出一个键值对，以元组形式返回
# print(d.popitem())
# dd = {"a":"b","c":"d"}
# #添加新元素
# d["a"] = 1
# d["b"] = 2

# import jieba
# #精确模式，返回一个列表类型的分词结果
# # jieba.lcut(s)
# print(jieba.lcut("python是一门编程语言"))
# #全模式，返回一个列表的分词结果，存在冗余
# # jieba.lcut(s,cut_all=True)
# print(jieba.lcut("python是一门编程语言",cut_all=True))
# #搜索引擎模式，返回一个列表类型的分词结果，存在冗余
# print(jieba.lcut_for_search("python是一门编程语言"))
# #想分词词典增加新词w
# # jieba.add_word(w)
# jieba.add_word("啦啦啦")
# print(jieba.lcut("python是一门编程语言啦啦啦啦"))

# def getText():
#     txt = open("D:\\Python\\hamlet.txt","r").read()
#     txt = txt.lower()
#     for ch in '|"!#$%()*+,-./;:<=>?@[\\]^_{|}~':
#         txt = txt.replace(ch," ")
#     return txt
# hamletTxt = getText()
# words = hamletTxt.split()
# counts = {}
# for word in words:
#     counts[word] = counts.get(word,0)+1
# items = list(counts.items())
# items.sort( key = lambda x: x[1],reverse = True )
# for i in range(10):
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))
#
# import jieba
# txt = open("沉默的羔羊.txt","r",encoding="utf-8").read()
# words = jieba.lcut(txt)
# counts = {}
# for word in words:
#     if len(word) == 1:
#         continue
#     else:
#         counts[word] = counts.get(word,0) + 1
# items = list(counts.items())
# items.sort(key = lambda x:x[1],reverse=True)
# for i in range(15):
#     word,count = items[i]
#     print("{0:<10}{1:>5}".format(word,count))


dic = {}
s = input()
x = eval(s)
try:
    for i in x:
        dic[x[i]] = i
    print(dic)
except:
    print("输入错误")


