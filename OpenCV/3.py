import cv2
import numpy as np

def cv_show(name,res):
    cv2.imshow(name,res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# #Canny边缘检测
# img = cv2.imread('1.jpg')
# cv_show('img',img)
# v1 = cv2.Canny(img,100,200)
# v2 = cv2.Canny(img,50,100)
#
# res = np.hstack((v1,v2))
# cv_show('res',res)
#
# #上采样 变大
# img = cv2.imread('pic.png')
# cv_show('img',img)
# up = cv2.pyrUp(img)
# cv_show('up',up)
# # #下采样 变小
# down = cv2.pyrDown(img)
# cv_show('down',down)
# cv2.imwrite('PIC.png',down)
# #
# #拉普拉斯金字塔
# down = cv2.pyrDown(img)
# down_up = cv2.pyrUp(down)
# l_l = img - down_up
# cv_show('l_l',l_l)

# #轮廓检测
# img = cv2.imread('TX.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# # 二值化处理 阈值127 maxval255
# ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# # cv_show('thresh',thresh)
# binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

# #binary,contours,hierachy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# #注意要copy,不然原图会变
# draw_img = img.copy()
# res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
# cv_show('res',res)


# img = cv2.imread('TX.jpg')
# cv_show('Tx',img)
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #二值图
# ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# # # cv_show('thresh',thresh)
# #轮廓检测
# #binary图像本身 contours轮廓 hierarchy每条轮廓的属性
# #hierarchy本身包含两个ndarray，每个ndarray对应一个轮廓，每个轮廓有四个属性
# binary,contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# # #绘制轮廓
# # #传入绘制图像，轮廓，轮廓索引，颜色模式，线条厚度
# # #注意copy,否则会变化原图
# # #-1是全部轮廓，可以按照索引0，1，2...
# draw_img = img.copy()
# #-1 代表全部 可以指定0，1...只显示那一个轮廓
# res = cv2.drawContours(draw_img,contours,-1,(0,0,255),2)
# cv_show('res',res)

# #第n个轮廓
# img = cv2.imread('1.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# ret,thresh = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
# binary,countours,hierarch = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# cnt = countours[8]
# draw_img = img.copy()
# res = cv2.drawContours(draw_img,[cnt],-1,(0,0,255),2)
# cv_show('res',res)

# #轮廓特征
# cnt = contours[0]
# #面积
# a=cv2.contourArea(cnt)
# print(a)
# #周长 True表闭合
# print(cv2.arcLength(cnt,True))
#
# #轮廓近似 x越小越近似
# epsilon = 0.02*cv2.arcLength(cnt,True)
# approx = cv2.approxPolyDP(cnt,epsilon,True)
#
# draw_img = img.copy()
# res = cv2.drawContours(draw_img,[approx],-1,(0,0,255),2)
# cv_show('res',res)
#
# #边界矩形轮廓
# x,y,w,h = cv2.boundingRect(cnt)
# img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
# cv_show('img',img)

# area = cv2.contourArea(cnt)
# x,y,w,h = cv2.boundingRect(cnt)
# rect_area = w * h
# extent = float(area) / rect_area
# print("轮廓面积与边界矩形比",extent)

#Sobel算子
img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
soblex = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=3)
soblex = cv2.convertScaleAbs(soblex)
sobley = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=3)
sobley = cv2.convertScaleAbs(sobley)
soblexy = cv2.addWeighted(soblex,0.5,sobley,0.5,0)

soblexy2 = cv2.Sobel(img,cv2.CV_64F,1,1,ksize=3)
soblexy2 = cv2.convertScaleAbs(soblexy2)

res = np.hstack((img,soblexy,soblexy2))
cv_show('img',res)

# #Scharr算子
img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Scharr(img,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(img,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)

res = np.hstack((img,scharrxy))
cv_show('img',res)
#
#拉普拉斯算子
img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

res = np.hstack((img,soblexy,scharrxy,laplacian))
cv_show('res',res)



