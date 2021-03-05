import numpy as np

# #只能有效存取和读取一维和二维数据
a = np.arange(100).reshape(5,20)
# #用delimiter分割，默认为空格
# np.savetxt('a.csv',a,fmt='%d',delimiter=',')
# #unpack=True 读入属性将写入不同变量
# b = np.loadtxt('a.csv',dtype=np.int,delimiter=',')
# print(b)

# #可以存取和读取多维数据
# #数据写入文件
# #sep数据分隔符，默认空格  format写入数据的格式
# a.tofile("b.dat",sep=',',format='%d')
# #count读入元素个数 -1代表整个文件
# b = np.fromfile("b.dat",dtype=float,count=-1,sep=',')
# print(b)
#
#Numpy的便捷文件存取
#以.npy为扩展名
# np.save('a.npy',a)
# b = np.load('a.npy')
# print(b)
#以,npz为扩展名，压缩
# np.savez('a.npz',a)
# b = np.load('a.npz')
# #.npz结尾的数据集是压缩文件
# #使用.files 命令进行查看文件内部
# print(b.files)
#
# print(b['arr_0'])
#随机数
#根据d0-dn创建随机数数组，浮点数[0,1)均匀分布
# rand()
# a = np.random.rand(1,2,3)
# print(a)
# # #根据d0-dn创建随机数数组，标准正太分布
# # randn()
# a = np.random.randn(1,2,3)
# print(a)
# # #根据shape创建随机整数或整数数组，范围是[low,hight)
# # randint(low[,hight,shape])
# a = np.random.randint(100,200,(3,4))
# print(a)
# #随机数种子，s是给定的种子值
# seed(s)
# np.random.seed(10)
# a = np.random.randint(100,200,(3,4))
# print(a)
#
# a = np.random.randint(100,200,(3,4))
# print(a)
# #根据数组a的第一轴进行排列，改变数组x
# # shuffle(x)
# np.random.shuffle(a)
# print(a)
#
# #根据数组a的第一轴产生一个新的乱序数组，不改变数组x
# # permutation(a)
# b = np.random.permutation(a)
# print(a)
# print(b)

# #从一维数组a中以概率p抽取元素，形成size形状新数组
# #replace表示是否可以重用元素，默认是True
# # choice(a,[size,replace,p])
# a = np.random.randint(100,200,(8,))
# print(a)
# b = np.random.choice(a,(3,2))
# print(b)
# b = np.random.choice(a,(3,2),replace=False)
# print(b)
# #元素出现次数越多，被抽取的概率越高
# b = np.random.choice(a,(3,2),p=a/np.sum(a))
# print(b)

# #产生具有均匀分布的数组，low起始值，hight结束值，size形状
# # uniform(low,hight,size)
# u = np.random.uniform(0,10,(3,4))
# print(u)
# #产生具有正态分布的数组，loc均值，scale标准差，size形状
# # normaml(loc,scale,size)
# u = np.random.normal(10,5,(3,4))
# print(u)
#
# #产生具有泊松分布的数组，lam随机时间发生率，size形状
# # poisson(lam,size)
# u = np.random.poisson(2,(3,4))
# print(u)

# 统计函数
# a = np.arange(15).reshape(3,5)
# print(a)
# #根据给定轴axis计算数组a相关元素之和，axis整数或元组
# # sum(a,axis=None)
# print(np.sum(a))
# #根据给定轴axis计算数组a相关元素的期望，axis整数或元组
# # mean(a,axis=None)
# print(np.mean(a))
# #在第一个维度做平均值
# print(np.mean(a,axis=0))
# #在第二个维度做平均值
# print(np.mean(a,axis=1))
# a = np.arange(15).reshape(3,5)
# print(a)
# print(np.sum(a))
# print(np.sum(a,axis=0))
# print(np.sum(a,axis=1))
# print(np.mean(a))
# print(np.mean(a,axis=0))
# print(np.mean(a,axis=1))


#根据给定轴axis计算数组a相关元素的加权平均值,weight是权重
# average(a,axis=None,weights=None)
# print(np.average(a))
#
# print(np.average(a,axis=0,weights=[1,2,3]))

#根据给定轴axis计算数组a相关元素的标准差
# std(a,axis=None)

#根据给定轴axis计算数组a相关元素的方差
# var(a,axis=None)


# a = np.arange(12).reshape(3,4)
# print(a)
# #计算数组中元素的最大值
# # max(a)
# print(np.max(a))
# #计算数组中元素的最小值
# # min(a)
# print(np.min(a))
# #计算数组中元素的最小值的降一维后下标
# #argmin(a)
# print(np.argmin(a))
# #计算数组中元素的最大值的降一维后下标
# #argmax(a)
# print(np.argmax(a))
# #根据shape将一维下标index转换成多维下标
# #unravel_index(index,shape)
# print(np.unravel_index(10,(4,3)))
# print(np.unravel_index(np.argmax(a),(4,3)))
# #计算数组a中元素最大值与最小值的差
# #ptp(a)
# print(np.ptp(a))
# #计算数组a中元素的中位数(中值)
# #median(a)
# print(np.median(a))

#梯度函数
#计算数组f中元素的梯度，当a为多维时，返回每个维度的梯度
#梯度：连续值之间的变化率，即斜率
a = np.random.randint(0,20,(3,2))
print(a)
x,y = np.gradient(a)
print(x)
print(y)

# b = np.random.randint(0,20,(5))
# print(b)
# print(np.gradient(b))