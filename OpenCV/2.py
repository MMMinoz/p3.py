import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#均值滤波
#简单的平均卷积操作
img = cv2.imread("ZS.png")
blur = cv2.blur(img,(3,3))
cv_show('img',blur)

#方框滤波
#基本和均值一样，(可以选择归一化，容易越界)
#越界取255
box = cv2.boxFilter(img,-1,(3,3),normalize=True)
cv_show('img',box)

#高斯滤波
aussian = cv2.GaussianBlur(img,(3,3),1)
cv_show('img',aussian)

#中值滤波
#相当于用种植代替
median = cv2.medianBlur(img,5)
cv_show('img',median)


res = np.hstack((blur,aussian,median))
# res = np.vstack((blur,aussian,median))

cv_show('res',res)