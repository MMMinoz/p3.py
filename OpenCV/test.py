import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

img = cv2.imread('pic.png')
kernel = np.ones((3,3),np.uint8)
erode = cv2.erode(img,kernel,iterations=1)
res = np.hstack((img,erode))
cv_show('res',res)

img = cv2.imread('pic.png')
kernel = np.ones((3,3),np.uint8)
dilate = cv2.dilate(img,kernel,iterations=1)
res = np.hstack((img,dilate))
cv_show('res',res)