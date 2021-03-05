import cv2
import numpy as np
import matplotlib.pylab as plt

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

#sift特征值

img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#得到特征值
#创建sift特征检测器
sift = cv2.xfeatures2d.SIFT_create()
#利用detect方法提取对象关键点
kp = sift.detect(gray,None)

#绘制特征点
img = cv2.drawKeypoints(gray,kp,img)
cv_show('img',img)
cv2.destroyAllWindows()

#计算特征值
kp,des = sift.compute(gray,kp)
print(np.array(kp).shape)
print(des.shape)
print(des[0])

