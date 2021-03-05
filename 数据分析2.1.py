import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import matplotlib.gridspec as gridspec

#plt.plot(x,y,format_string,**kwargs)
#x:x轴数据，列表或数组，可选
#y:y轴数据，列表或数组
#format_string：控制曲线的格式字符串，可选
#**kwargs:第二组或更多(x,y,format_string)
#当控制多条曲线时,各x不能省略

#x省略
# plt.plot([3,1,4,5,2])
# plt.ylabel("grade")
# #默认png文件，可通过dpi改变输出质量
# plt.savefig('test',dpi=600)
# plt.savefig('test.jpg',dpi=600)
# plt.axis([-1,5,0,6])
# plt.show()

# plt.plot([0,2,4,6,8],[3,1,4,5,2])
# plt.ylabel("Grade")
# #设置x轴y轴坐标起始
# #x轴从-1开始，10结束
# #y轴从0开始，6结束
# plt.axis([-1,10,0,6])
# plt.show()

#plt.subplot(n,m,x)
# def f(t):
#     return np.exp(-t) * np.cos(2 * np.pi * t)
#
# a = np.arange(0.0,5.0,0.02)
# b = np.arange(0.0,5.0,0.02)
#
# plt.subplot(211)
# plt.plot(a,f(a))
#
# plt.subplot(2,1,2)
# plt.plot(a,np.cos(2*np.pi*b),'r--')
# plt.show()

#色彩风格标志等
# a = np.arange(10)
# plt.plot(a,a*1.5,'go:',a,a*2.5,'rx--',a,a*3.5,'^-.',a,a*4.5,'*')
# plt.show()
# x = np.arange(0,12,2)
# plt.plot(x,x*1.5,'*',x,x*2.5,'go:',x,x*3.5,'^--',x,x*4.5,'rx-.')
# plt.show()
# #plot中文显示
##全局
# matplotlib.rcParams['font.family'] = 'SimHei'
# matplotlib.rcParams['font.size'] = 10
# #
# plt.plot([3,1,4,5,2])
# plt.ylabel("纵轴(值)")
# plt.xlabel("横轴(变量)")
# plt.show()

# #局部
# plt.plot([3,1,4,5,2],'r-.')
# plt.title('坐标轴',fontproperties='SimHei',fontsize=20)
# plt.ylabel('纵轴(值)',fontproperties='SimHei',fontsize=10)
# plt.xlabel('横轴(变量)',fontproperties='SimHei',fontsize=10)
# # plt.text(2,1,r'$\mu=100$',fontsize=15)
# #xy是箭头所在位置 xytext是文本所在位置
# #shrink 箭头到文字有空白
# plt.annotate(r'$\mu=100$',xy=(3,3),xytext=(3,1.5),\
#              arrowprops=dict(facecolor='black',shrink=0.1,width=2))
# # #表格
# plt.grid(True)
# plt.show()

# #自定义子区域
# #第一个元组：把整个画布分成几行几列
# #第二个元组：此自定义网格的起始位置
# #colspan占列宽度    row占行宽度
# plt.subplot2grid((3,3),(0,0),colspan=3)
# plt.subplot2grid((3,3),(1,0),colspan=2)
# plt.subplot2grid((3,3),(2,0))
# plt.subplot2grid((3,3),(2,1))
# plt.subplot2grid((3,3),(1,2),rowspan=2)
# plt.show()


# gs = gridspec.GridSpec(3,3)
# ax1 = plt.subplot(gs[0,:])
# ax2 = plt.subplot(gs[1,:2])
# ax3 = plt.subplot(gs[2,:1])
# ax4 = plt.subplot(gs[2,1:2])
# ax5 = plt.subplot(gs[1:,-1])
# plt.show()

# #饼图
# labels = 'Frogs','Hogs','Dogs','Logs'
# #饼图所占比例
# sizes = [15,30,45,10]
# #饼图某部分突出
# explode = (0,0.1,0,0)
#
# plt.pie(sizes,explode=explode,labels=labels,autopct='%.1f%%',
#         shadow=False,startangle=90)
# # plt.axis('equal')
# plt.show()
# print("ok")

# #直方图
# temp = [8,9,13,18,23,27]
# x = np.arange(1,7)
# plt.bar(x,temp)
# plt.xlabel("月",fontproperties='SimHei')
# plt.show()

# #散点图
# x = np.arange(20)
# y = x * 1.5
# plt.scatter(x,y,marker='*')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title('Scatter')
# plt.show()

# #折线图
#
# def ran():
#     a = []
#     for i in range(20):
#         a.append(np.random.randint(0,20))
#     return a
# x = np.arange(20)
# y = ran()
# plt.plot(x,y)
# plt.grid()
# plt.show()

x = [1, 2, 3, 4]
y = [1, 4, 9, 6]
lables = ['Frogs', 'Hogs', 'Bogs', 'Slogs']
plt.plot(x, y)
#x代表x坐标轴的位置，lable代表某位置的显示lable，rotation代表lable显示的旋转角度。
plt.xticks(x, lables, rotation='vertical')
plt.margins(0.2)
plt.subplots_adjust(bottom=0.15)
plt.show()

# #直方图hist
# def ran():
#     a = []
#     for i in range(100):
#         a.append(np.random.randint(1,101))
#     return a
# ages = ran()
# plt.hist(ages,bins=10,rwidth=0.8)
# plt.show()