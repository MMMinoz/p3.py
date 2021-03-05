import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img = cv2.imread("1.jpg")
# cv_show("img",img)
# img = cv2.imread("1.jpg",0)
# cv_show("img",img)

# #灰度视频
# vc = cv2.VideoCapture('D:\\Python\\Pic\\test.mp4')
# if vc.isOpened():
#     open,frame = vc.read()
# else:
#     open = False
# while open:
#     ret,frame = vc.read()
#     if frame is None:
#         break
#     if ret == True:
#         gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('result',gray)
#         if cv2.waitKey(10) & 0xFF == 27:
#             break
# vc.release()
# cv2.destroyAllWindows()

# img = cv2.imread("1.jpg")
# cat = img[0:50,20:70]
# cv_show("cat",cat)

# #提取颜色通道
# img = cv2.imread("1.jpg")
# b,g,r = cv2.split(img)
# print(b)
# print(g)
# print(r)
# # #b
# print(img[:,:,0])
# #g
# print(img[:,:,1])
# #r
# print(img[:,:,2])
#
# img2 = img.copy()
# img2[:,:,0] = 0
# img2[:,:,1] = 0
# cv_show("img2",img2)

# #根据bgr合成图片
# img = cv2.merge((b,g,r))
# cv_show('img',img)

# #边界填充
# img = cv2.imread('D:\Python\Pic\dog.jpg')
# top_size,bottom_size,left_size,right_size =(50,50,50,50,)
# replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
# replicate = cv2.cvtColor(replicate,cv2.COLOR_BGR2GRAY)
# reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value = 0)
#
# #cv2是bgr，plt是rgb,调整以便让plt显示img原图
# b,g,r = cv2.split(img)
# img = cv2.merge((r,g,b))
#
# plt.subplot(231),plt.imshow(img),plt.title('ORIGINAL')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('replicate')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('reflect')
# plt.subplot(234),plt.imshow(reflect101),plt.title('reflect101')
# plt.subplot(235),plt.imshow(wrap),plt.title('wrap')
# plt.subplot(236),plt.imshow(constant),plt.title('constant')
#
# plt.show()

# #图像融合
# img1 = cv2.imread('1.jpg')
# img2 = cv2.imread('test.jpg')
# a,b,c = img1.shape
# print(img1.shape)
# img2 = cv2.resize(img2,(b,a))
# print(img2.shape)
# res = cv2.addWeighted(img1,0.6,img2,0.4,0)
# cv_show('res',res)
