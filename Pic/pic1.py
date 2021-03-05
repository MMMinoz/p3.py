import cv2
import numpy as np
import matplotlib.pylab as plt

#展示图片
def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# img=cv2.imread('test.jpg')
# print(img.shape)
# cv_show('test',img)

#获取图片属性
# img.shape #返回（长，宽，通道）
# img.size #返回图片总像素数值
# img.dtype #返回图片数据类型

#灰度图
# imgG=cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
# print(imgG.shape)
# cv_show('testG',imgG)
# cv2.imwrite('testG.jpg',imgG)

#利用图片播放视频
# vc = cv2.VideoCapture('test.mp4')
# if not vc.isOpened():
#     open = False
# else:
#     #vc.read()会返回两个值
#     # open是布尔值，如果读取帧是正确的则返回True，如果文件读取到结尾返回值为False
#     # frame该帧图像的三维矩阵BGR形式
#     open,frame = vc.read()
# while open:
#     ret,frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('result',gray)
#         if cv2.waitKey(10)&0xFF == 7:
#             break
# vc.release()
# cv2.destroyAllWindows()

# #利用分片 截取部分图像
# img=cv2.imread('dog.jpg')
# # test=img[0:200,0:200]
# # cv_show('test',test)
#
# #颜色通道提取
# b,g,r=cv2.split(img)
# print(r.shape)
# #颜色通道组合
# img=cv2.merge((b,g,r))
# print(img.shape)
# #只保留某通道R_img[:,:,X]!=0
# R_img=img.copy()
# R_img[:,:,0]=0
# R_img[:,:,1]=0
# cv_show( 'R',R_img)
#
# #边界填充
# top_size,bottom_size,left_size,right_size = (50,50,50,50)
# replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
# # cv_show('1.jpg',replicate)
# reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
# # cv_show('2.jpg',reflect)
# reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)
# # cv_show('3.jpg',reflect)
# wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
# # cv_show('4.jpg',wrap)
# constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=0)
# # cv_show('5.jpg',constant)
#
# #在同一张画布上显示多个图，plt.subplot(2,3,1)==plt.subplot(231),,三个整数是行数、列数和索引值
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('reflect101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('wrap')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('constant')
#
# plt.show()

# #数值计算  所有像素点+X [0,255],越界X%255
# img_cat = cv2.imread('cat.jpg')
# img_dog = cv2.imread('dog.jpg')
# img_cat2 = img_cat+200
# print(img_cat)
# print(img_cat2)
#
# #数值计算  所有像素点+X [0,255]越界取255
# img_cat3 = cv2.add(img_cat,img_cat2)
# print(img_cat3)

#图像融合
#更改shape
# a,b,c=img_cat.shape
# print(img_dog.shape)
# # cv_show('dog',img_dog)
# img_dog = cv2.resize(img_dog,(b,a))
# print(img_dog.shape)
# cv_show('dog',img_dog)
#按比例更改shape
# res = cv2.resize(img,(0,0),fx=1,fy=13)
# cv_show('res',res)

# 图像融合 R=at1+bt2+c
# 一张图是t1，另一张是t2
# a是t1的权重,b是t2的权重
# C提亮
# res=cv2.addWeighted(img_cat,0.6,img_dog,0.4,0)
# cv_show('res',res)


# vc = cv2.VideoCapture('D:\\Python\\Pic\\test.mp4')
# if vc.isOpened():
#     open,frame = vc.read()
# else:
#     open = False
# while open:
#     open,res = vc.read()
#     if res is None:
#         break
#     else:
#         gray = cv2.cvtColor(res,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('res',gray)
#         if cv2.waitKey(10) & 0xFF == 27:
#             break
