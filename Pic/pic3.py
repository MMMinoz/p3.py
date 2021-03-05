import cv2
import numpy as np
import matplotlib.pylab as plt

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

#模板匹配
#1.读入原图和模板图，并变成灰度图
#2.使用shape得到模板图的h,w
#3.使用6种方法(之一)进行模板匹配
#4.利用minMaxLoc()得到min_val,max_val,min_loc,max_loc
#  若使用SQDIFF相关方法，则选择min_loc
#  若使用其他方法，则选择max_loc
#5.利用min_loc(max_loc)坐标得到top_lfet坐标
#  再利用top_left[0](left)+w得到bottom_right(right)
#  再利用top_left[1](top)+h得到bottom_right(bottom)
#  得到bottom_right坐标
#6.在原图上画外接矩形，以top_left,bottom_right为坐标
#7.最后利用plt.suplot(),plt.imshow(),plt.show()展示


# #利用imread第二个参数为0变成灰度图
# img = cv2.imread('dog.jpg',0)
# template = cv2.imread('dog1.jpg',0)
# h,w = template.shape
#
# print(img.shape)
# print(template.shape)
#
# #相关度
# methods={'cv2.TM_CCOEFF',#越大越相关
# 'cv2.TM_CCOEFF_NORMED',#1
# 'cv2.TM_CCORR',#越大越相关
# 'cv2.TM_CCORR_NORMED',#1
# 'cv2.TM_SQDIFF',##越小越相关
# 'cv2.TM_SQDIFF_NORMED'}#0
#
# for meth in methods:
#     img2 = img.copy()
#
#     #匹配方法的真值
#     method = eval(meth) #eval函数将字符转化为可执行代码
#     print(method)
#     #res是一个结果矩阵,shape为（a1-a2+1,b1-b2+1）
#     res = cv2.matchTemplate(img,template,method)
#
#     min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
#
#     #如果是平方差匹配或TM_SQDIFF匹配 取小值
#     if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
#         top_left = min_loc
#     else:
#         top_left = max_loc
#     bottom_right = (top_left[0]+ w,top_left[1] + h)
#
#     #画矩形
#     cv2.rectangle(img2,top_left,bottom_right,(0,0,255),3)
#
#     plt.subplot(121),plt.imshow(img,'gray')
#     plt.xticks([]),plt.yticks([])#隐藏坐标轴
#     plt.subplot(122),plt.imshow(img2,'gray')
#     plt.xticks([]), plt.yticks([])
#     plt.suptitle(meth)
#
#     plt.show()

#1.读入原图和模板图，并变成灰度图
#2.使用shape得到模板图的h,w
#3.使用6种方法(之一)进行模板匹配
#4.设置阈值threshold，并利用np.where(res>=threshold)或np.where(res<=threshold)得到有效矩阵loc
#5.利用zip(*loc[::-1])遍历全部匹配图形做外接矩形
#6.展示






#多模板匹配
img_rgb = cv2.imread('ml.jpg')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('ml1.jpg',0)

w, h = template.shape

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

threshold = 0.9#1
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 3)

plt.subplot(1,2,1),plt.imshow(img_gray)
plt.xticks([]),plt.yticks([])#隐藏坐标轴

plt.subplot(1,2,2),plt.imshow(img_rgb)#loc[::-1]将输出的索引变换成x,y坐标，因为索引和x,y坐标是正好相反的，所以要对换下位置。然后再循环坐标，分别画出红色边界。
plt.xticks([]),plt.yticks([])#隐藏坐标轴

plt.show()