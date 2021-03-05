import cv2
import numpy as np
import matplotlib.pylab as plt

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(1000)
    cv2.destroyAllWindows()

#harris角点检测
img = cv2.imread('chess.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

## 输入图像必须是 float32 ,最后一个参数在 0.04 到 0.06 之间
dst = cv2.cornerHarris(gray,2,3,0.04)
print('dst.shape:',dst.shape)

img[dst>0.001*dst.max()]=[0,0,255]
cv_show('dst',img)
cv2.destroyAllWindows()