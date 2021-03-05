import numpy as np
import matplotlib.pyplot as plt

# x = np.arange(0,12,2)
# y = x*0.5
# plt.axis([0,10,0,10])
# print(x)
# print(y)
# plt.plot(x,y,'r-.')
# plt.title("Label")
# plt.xlabel("X-横轴",fontproperties='SimHei',fontsize=15)
# plt.ylabel("Y-纵轴",fontproperties='SimHei',fontsize=15)
# plt.text(8,8,"这是一个坐标轴",fontproperties='SimHei',fontsize=10)
# plt.annotate('Y=X*0.5',fontsize=10,xy=(5,2.5),xytext=(5,5),\
#              arrowprops=dict(facecolor='black',shrink=0.1,width=0.5))
# plt.grid()
# plt.show()

# plt.subplot2grid((3,3),(0,0),colspan=3)
# plt.subplot2grid((3,3),(1,0),colspan=2)
# plt.subplot2grid((3,3),(2,0))
# plt.subplot2grid((3,3),(2,1))
# plt.subplot2grid((3,3),(1,2),rowspan=2)
# plt.show()

import matplotlib.gridspec as grisdpec

gs = grisdpec.GridSpec(3,3)
plt.subplot(gs[0,:])
plt.subplot(gs[1,:2])
plt.subplot(gs[2,:1])
plt.subplot(gs[2,1:2])
plt.subplot(gs[1:,-1])
plt.show()