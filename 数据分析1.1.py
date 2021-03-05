import numpy as np

# list =[0,1,2,3]
# #从列表类型建立
# x = np.array(list)
# print(x)
#
# #从元组类型建立

# x = np.array((4,5,6,7))
# print(x)
#
# #从列表和元组混合类型创建
# #所包含数据个数相同就可混合使用
# x = np.array([list,(4,5,6,7)] ,dtype=np.float32)
# print(x)
#
# #类似range()
# x = np.arange(10)
# print(x)
#
# #(m,n)的全1矩阵，默认浮点数
# x = np.ones((3,6))
# print(x)
#
# x = np.ones((2,3,4))
# print(x)
# print(x.shape)

# (m,n)的全0矩阵，默认浮点数
# x = np.zeros((3,6),dtype = np.int32)
# print(x)

# n*n的对角为1的对角矩阵
# x = np.eye(5)
# print(x)
#
# #根据shape生成一个数组，每个元素至都是val
# x = np.full((3,4),5)
# print(x)
#
# 根据数组x的形状生成一个全1数组
# x = np.full((3,4),5)
# a = np.ones_like(x)
# print(a)
#
# #根据数组x的形状生成一个全0数组
# a = np.zeros_like(x)
# print(a)
#
# 根据数组x的形状生成一个数组,值为val
# a = np.full_like(x,2)
# print(a)
#
# #根据起止数据等间距的填充数据，形成数组
# x = np.linspace(1,10,4)
# print(x)
# endpoint表示10是否是生成元素中的一个,默认True
# x = np.linspace(1,10,4,endpoint=False)
# print(x)

# 将两个或多个数组合并成一个新的数组，默认axsi=0

# x = np.full((1,2),5)
# a = np.ones_like(x)
# print(x)
# print(a)
# x = np.concatenate((a,x))
# print(x)
#
# x = np.full((2,3),5)
# a = np.full((2,3),1)
# print(x)
# print(a)
# x = np.concatenate((a,x),axis=1)
# print(x)

# b = np.full((2,1,3),5)
# a = np.full((2,1,3),1)
# print(b)
# print(a)
# print("---------------------------")
# x = np.concatenate((a,b),axis=0)
# print(x)
# print("---------------------")
# x = np.concatenate((a,b),axis=1)
# print(x)
# print("---------------------")
# x = np.concatenate((a,b),axis=2)
# print(x)

# 变换
# x = np.ones((2,3,4),dtype=np.int32)
# print(x)
# #不改变数组元素，返回一个shape形状的数组，原数组不变
# a = x.reshape((3,8))
# print(x)
# print(a)
#
# #与.reshape()功能一致，但修改原数组
# x = np.ones((2,3,4),dtype=np.int32)
# print(x)
# a = x.resize((3,8))
# print(x)
# print(a)
# #
# 将数组n个维度中的两个维度调换
# x = x.swapaxes(0,2)
# print(x)
# #对数组进行降维，返回折叠后的一维数组，原数组不变
# a = x.flatten()
# print(x)
# print(a)
# 转置
# x = x.transpose((2,1,0))
# print(x)
#
# 类型转换
# #.astype()一定会创建一个新的数组，即使类型一样
# a = np.ones((2,3,4),dtype=np.int32)
# print(a)
# b = a.astype(np.float)
# print(b)
#
# #数组转换成列表
# b = a.tolist()
# print(b)
#
#
# a = np.arange(24).reshape((2,3,4))
# 索引
# print(a)
# print(a[1,2,3])
# print(a[0,1,2])
# print(a[-1,-2,-3])
#
# #切片
# print(a[:,1,-3])
# print(a[:,1:3,:])#第二个维度内切片 和list类似[a:b]即在区间[a,b)内
# print(a[:,:,::2])#和list类似，步长

# #运算
# #数组与标量之间的运算
# #数组与标量之间的运算作用于数组的每一个元素
# a = np.arange(1,25).reshape((2,3,4))
# print(a)
# #a.mean() a所有元素的平均数
# print(a.mean())
# a = a/a.mean()
# print(a)
# x = np.arange(24).reshape((2,3,4))
# print(a)
# print(a/4)


a = np.arange(1, 25).reshape((2, 3, 4))
# print(np.abs(a))
# print("-----------------------------")
# print(np.fabs(a))
# print("-----------------------------")
# print(np.sqrt(a))
# print("-----------------------------")
# print(np.square(a))
# print("-----------------------------")
# print(np.log(a))
# print("-----------------------------")
# print(np.log10(a))
# print("-----------------------------")
# print(np.log2(a))
# print("-----------------------------")
# print(np.ceil(a))
# print("-----------------------------")
# print(np.floor(a))
# print("-----------------------------")
# a, b = np.modf(a)
# print("整数部分：")
# print(a)
# print("小数部分：")
# print(b)

b = np.square(a)
print(b)
#元素的最大值计算
print(np.maximum(a,b))
print(np.fmax(a,b))
# #元素的最小值计算
print(np.minimum(a,b))
print(np.fmin(a,b))
#元素的模运算
#a中元素对b中元素取模
print(np.mod(a,b))
#b中元素对a中元素取模
print(np.mod(b,a))
# 将数组b中的个元素的符号赋值给数组a对应元素
b = -b
print(np.copysign(a,b))
