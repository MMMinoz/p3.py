import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# #图像腐蚀
# img = cv2.imread('dige.png')
# cv_show('img',img)
# #(5,5)的全1矩阵
# kernel = np.ones((5,5),np.uint8)
#
# erosion = cv2.erode(img,kernel,iterations = 1)
# cv_show('erosion',erosion)
#
# pie = cv2.imread('pie.png')
# kernel = np.ones((30,30),np.uint8)
# erosion_1 = cv2.erode(pie,kernel,iterations=1)
# erosion_2 = cv2.erode(pie,kernel,iterations=2)
# res = np.hstack((pie,erosion_1,erosion_2))
# cv_show('img',res)

# #图像膨胀
# img = cv2.imread('dige.png')
# cv_show('img',img)
# kernel = np.ones((5,5),np.uint8)
# dige_erosion = cv2.erode(img,kernel,iterations=1)
# cv_show('img',dige_erosion)
#
# kernel = np.ones((5,5),np.uint8)
# dige_dilate = cv2.dilate(dige_erosion,kernel,iterations=1)
# cv_show('img',dige_dilate)
#
# pie = cv2.imread('pie.png')
# cv_show('img',pie)
# kernel = np.ones((30,30),np.uint8)
# erosion_1 = cv2.dilate(pie,kernel,iterations=1)
# erosion_2 = cv2.dilate(pie,kernel,iterations=2)
# res = np.hstack((pie,erosion_1,erosion_2))
# cv_show('img',res)

#开运算 闭运算
#开运算 先腐蚀再膨胀
# #图像腐蚀
img = cv2.imread('pic.png')
kernel = np.ones((5,5),np.uint8)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
res = np.hstack((img,opening))
cv_show('img',res)

#闭运算 先膨胀再腐蚀
img = cv2.imread('pic.png')
kernel = np.ones((5,5),np.uint8)
closeing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
res = np.hstack((img,closeing))
cv_show('img',res)

#梯度运算
pie = cv2.imread('pie.png')
kernel = np.ones((7,7),np.uint8)
erosion = cv2.erode(pie,kernel,iterations=5)
dilate = cv2.dilate(pie,kernel,iterations=5)

res = np.hstack((erosion,dilate))
cv_show('res',res)

#梯度运算像用膨胀-腐蚀
gradient = cv2.morphologyEx(pie,cv2.MORPH_GRADIENT,kernel)
cv_show('img',gradient)
cv_show('img',dilate-erosion)

#礼帽 黑帽
#礼帽：原始输入-开运算
# img = cv2.imread('dige.png')
# tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
#
# opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
# tophat_1 = opening -img
# res = np.hstack((tophat,tophat_1))
# cv_show('res',res)
img = cv2.imread('dige.png')
tophat = cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
res = np.hstack((img,tophat))
cv_show('res',res)
#黑帽：闭运算-原始输入
img = cv2.imread('dige.png')
blackhat = cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

closeing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
blackhat_1 = img - closeing
res = np.hstack((img,blackhat))
cv_show('res',res)