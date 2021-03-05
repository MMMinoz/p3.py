import cv2
import numpy as np
import matplotlib.pylab as plt


def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

# img = cv2.imread('test.jpg',cv2.IMREAD_GRAYSCALE)
#
# #Canny边缘检测
# v1 = cv2.Canny(img,120,250) #minvalue，maxvalue
# v2 = cv2.Canny(img,50,100)
#
# res = np.hstack((v1,v2))
# cv_show('res',res)

# img = cv2.imread('test.jpg')
# # # cv_show('img',img)
# # print(img.shape)
#
# #上采样
# Up = cv2.pyrUp(img)
# # cv_show('Up',Up)
# print(Up.shape)
#
# #下采样
# Down = cv2.pyrDown(Up)
# # cv_show('Down',Down)
# print(Down.shape)
#
# res = np.hstack((img,Down))
# cv_show('res',res)

#二值图像
# img = cv2.imread('TX.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# # # cv_show('thresh',thresh)
# #
# binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
#
# # #绘制轮廓
# # #传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
# # #注意copy,否则会变化原图
# # #-1是全部轮廓，可以按照索引0，1，2...
# draw_img = img.copy()
# res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
# cv_show('res',res)

# #轮廓特征
# cnt = contours[0]
# # #面积
# a=cv2.contourArea(cnt)
# print(a)
# #周长 True表闭合
# print(cv2.arcLength(cnt,True))
# #轮廓近似
# img = cv2.imread('TX2.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cnt = contours[0]
# #
# draw_img = img.copy()
# res = cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)
# cv_show('res',res)
#
# epsilon = 0.015*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)
# draw_img = img.copy()
# res = cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)
# cv_show('res',res)

# #边界矩形(外界矩形)
# img = cv2.imread('TX.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cnt = contours[0]
#
# x,y,w,h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
# cv_show('img',img)
# b=(x+w)*(y+h)
# print(b)
# print(a/b)

# x,y,w,h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
# cv_show('img',img)

img = cv2.imread('1.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

dst = cv2.cornerHarris(gray,2,3,0.04)
img[dst > 0.01 * dst.max()] = [0,0,255]
cv_show('img',img)