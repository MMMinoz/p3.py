# print("Hey %d there." , 5)
# print("Hey %d there." % 5)
# print("Hey %s there." , "you")
# print("Hey %s there." % "you")

# for i in range(5):
#     print("hello:%d"%i)
# for i in range(5):
#     print("hello:",i)//逗号有空格

# a = 10
# print("Hey %d there." % a)
# print("Hey %d there." , a)
#
# print(format(1.4444))
# print("%r" % 1.5555)
# b=1.6666
# print("%r" %b)
# c = 'hello, {!r}'.format(1.777)
# print(c)
#
# text = 'Hello world'
# print('%r' % text)
# print('%s' % text)
# for i in range(0,5):
#     print(i,end=' ')
#
# formatter = "%r %r %r %r"
#

# T = input()
# if T[0] in ['R']:
#     C = eval(T[3:])/6.78
#     print("USD{:.2f}".format(C))
# elif T[0] in ['U']:
#     F = eval(T[3:])*6.78
#     print("RMB%.2f" % F)
# else:
#     print("")


# tem = "零一二三四五六七八九"
# str = input()
# for i in str:
#     print(tem[eval(i)],end="")


# print(0.1 + 0.2 == 0.3)
# print(round(0.1 + 0.2,1) == 0.3)
# print(round(0.111),round(0.111,1),round(0.111,2))
# print(0.1 + 0.2)
# z=9.6E5+3j
# print(z.real,z.imag)


# abs(-10.01)
# divmod(10,3)
# z = pow(2,10,3) #3可省略 z = pow(2,10) % 3
# print(z)
# complex(5)#变成虚数类型
# print(complex(5))



# def UP(df):
#     dayup=1
#     for i in range(365):
#         if i % 7 in [6,0]:
#             dayup *= 1-0.01
#         else:
#             dayup *= 1+df
#     return dayup
#
# df = 0.01
# while(UP(df) < 37.78):
#     df+=0.001
#     UP(df)
# print(df)

#chr(u)将unicode编码转换为对应字符
#ord(x)将字符转化为unicode编码
# for i in range(12):
#     print(chr(9800+i),end='  ')

# print("{1}计算机{0}的cpu占用率为{2}%".format("2018","C",10))
# print("{1:}计算机{0:}的cpu占用率为{2:}%".format("2018","C",10))
#
# print('hello, {}'.format(1.777))
# #print("{引导符号:填充/对齐/宽度/，/.精度/类型}.format(x))
#
#用=填充 对齐 宽度20
#对齐 ^居中，>右对齐，<左对齐

# print("{0:=^20}".format("Python"))
# print("{0:=>20}".format("Python"))
# print("{0:=<20}".format("Python"))
#
# {参数位置:填充符 对齐 宽度 数字的千位分隔符 .精度 类型}.format
# # #,数字中的千位分隔符
# print("{:,}".format(1000000))
# #.2保留精度
# print("{:.2f}".format(1.4444))
# #整数类型 b\c\d\o\x\X 浮点类型e\E\f\%
# print("{0:b},{0:c},{0:d},{0:o},{0:x},{0:X},{0:e},{0:E},{0:f},{0:%}".format(425))

# %Y年份 %m月份 %B月份名称 %b月份名简写 %d日期
# %A星期 %a星期简写 %H24制时间 %I12小时制时间
# %M分钟 %p上午下午 %S秒
# import time as t
#
# start = t.perf_counter()
#
# print(t.time())
# print(t.ctime())
# print(t.gmtime())
# time = t.gmtime()
# print(t.strftime("%Y-%m-%d %H:%M:%S",time))
# timestr = "2021-01-25 12:35:21"
# print(t.strptime(timestr,"%Y-%m-%d %H:%M:%S"))
# #程序休眠1秒
# t.sleep(1)
# end = t.perf_counter()
# stay = end - start
# print("共运行{}秒".format(stay))


# print("------执行开始------")
# scale = 10
# for i in  range(scale+1):
#     a = "*"*i
#     b = "."*(scale-i)
#     c = (i/scale)*100
#     print("{:.0f}%[{}->{}]".format(c,a,b))
#     t.sleep(0.1)
# print("------执行结束------")

# for i in range(101):
#     print("\r{:3}%".format(i),end='')
#     t.sleep(0.1)

# str = "AbCdEfG"
# print(str.lower(),str.upper())
#
# str = "A,B,C"
# print(str.split(","))
#
# str = "an apple a day"
# print(str.count("a"))
#
# #str.replace(old,new)
# s = "python"
# print(s.replace("p","P"))

#str.center(width,fillchar) 字符串根据宽度width居中，用fillchar来填充
# scale = 50
# print("执行开始".center(scale//2,"-"))
# start = t.perf_counter()
# for i in range(scale+1):
#     a = "*"*i
#     b = "."*(scale-i)
#     c = (i/scale)*100
#     dur = t.perf_counter()-start
#     print("\r{:^3.0f}%[{}->{}]{:.2f}s".format(c,a,b,dur),end='')
#     t.sleep(0.1)
#
# print("\n"+"执行结束".center(scale//2,'-'))

# str = input()
# for i in str:
#     if i.islower():
#            print(chr(ord('a')+(ord(i)-ord('a') + 3) % 26 ),end='')
#     elif i.isupper():
#         print(chr(ord('A')+(ord(i)-ord('A') + 3) % 26 ),end='')
#     else:
#         print(i,end='')


# a = pow(1.01,365)
# dayup = 1
# df = 0.01
# while dayup < a:
#     df += 0.001
#     dayup = 1
#     for i in range(0,365):
#         if i % 7 in [0,6]:
#            dayup = dayup * (1-0.01)
#         else:
#             dayup = dayup * (1+df)
# print(round(df,3))

# def dayUP(df):
#     dayup = 1
#     for i in range(365):
#         if i % 7 in [6,0]:
#             dayup = dayup*(1 - 0.01)
#         else:
#             dayup = dayup*(1 + df)
#     return dayup
# dayfactor = 0.01
# while dayUP(dayfactor) < 37.78:
#     dayfactor += 0.001
# print("工作日的努力参数是: {:.10f}".format(dayfactor))


# import random as ran
# #设置随机数种子
# ran.seed(10)
# print(ran.random())
# #随机产生一个[a,b]之间的整数
# print(ran.randint(1,10))
# #生成一个[m,n)之间以k为步长的随机整数
# print(ran.randrange(1,10,3))
# #生成一个比特为长k的随机数
# print(ran.getrandbits(16))
# #生成一个[a,b]之间的随机小数
# print(ran.uniform(1,10))
# #从序列s中随机选择一个元素
# s = [1,2,3,4,5,6,7,8,9,10]
# print(ran.choice(s))
# #将序列s中元素随机排列，返回打乱后的序列
# ran.shuffle(s)
# print(s)

# pi = 0
# n = 100
# #用\来换行 表示在同一行
# for k in range(n):
#      pi += 1/pow(16,k)*( \
#          4/(8*k+1) - 2/(8*k+4) - \
#          1/(8*k+5) - 1/(8*k+6))
# print("圆周率值是:{}".format(pi))

# import random as ran
# import time as t
# ran.seed(123)
# darts = eval(input())
# hits = 0.0
# start = t.perf_counter()
# for i in range(1,darts+1):
#     x,y = ran.random(),ran.random()
#     dist = pow(x**2+y**2,0.5)
#     if dist <=1.0: #利用到圆心的距离判断(x,y)是否在圆内
#         hits += 1
# pi = 4 * (hits/darts)
# print("圆周率值是:{}".format(pi))
# print("运行时间是:{}s".format(t.perf_counter()-start))


#七段数码管 绘制时间

# import turtle as tur
# import time
#
# def drawGap():
#     tur.penup()
#     tur.fd(5)
#
# def drawLine(draw):
#     drawGap()
#     tur.pendown() if draw else tur.penup()
#     tur.fd(40)
#     drawGap()
#     tur.right(90)
#
# def drawDigit(digit):
#     drawLine(True) if digit in [2, 3, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 2, 6, 8] else drawLine(False)
#     tur.left(90)
#     drawLine(True) if digit in [0, 4, 5, 6, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else drawLine(False)
#     drawLine(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else drawLine(False)
#     tur.left(180)
#     tur.penup()
#     tur.fd(20)
#
#
# def drawDate(date):
#     for i in date:
#         drawDigit(eval(i))
#
# def main():
#     tur.setup(800,350)
#     tur.penup()
#     tur.fd(-300)
#     tur.pensize(5)
#     date = time.strftime("%Y%m%d",time.gmtime())
#     print(date)
#     drawDate(date)
#     tur.done()
# main()

# import turtle
# def koch(size,n):
#     if n == 0:
#         turtle.fd(size)
#     else:
#         for angle in [0,60,-120,60]:
#             turtle.left(angle)
#             koch(size/3,n-1)
#
# turtle.setup(600,600)
# turtle.penup()
# turtle.goto(-200,150)
# turtle.pensize(3)
# turtle.pendown()
# level = 3
# koch(400,level)
# turtle.right(120)
# koch(400,level)
# turtle.right(120)
# koch(400,level)
#
# turtle.done()