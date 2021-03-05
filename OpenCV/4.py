import cv2
import numpy as np

def cv_show(name,img):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# #Harris角点检测  可处理图像是float32
# #读入图像变为灰度图 (转换为float32)
# #对图像进行角点检测
# #若dst>0则是角点 dst<0是边界 dst约等于0是内部
#
# img = cv2.imread('D:\\Python\\Pic\\chess.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# gray = np.float32(gray)
# dst = cv2.cornerHarris(gray,2,3,0.04)
# print(dst)
#
# #角点标红色
# img[dst>0.01*dst.max()] = [0,0,255]
# cv_show('img',img)

img1 = cv2.imread('1.jpg')
img2 = cv2.imread('1.jpg')
img = cv2.imread('1.jpg')

gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


sift = cv2.xfeatures2d.SIFT_create()

kp = sift.detect(gray,None)

img = cv2.drawKeypoints(gray,kp,img)
# cv_show('img',img)

kp,des = sift.compute(gray,kp)

kp1, des1 = sift.detectAndCompute(gray1,None)
img1 = cv2.drawKeypoints(gray1,kp1,img1)
cv_show('img',np.hstack((img,img1)))

kp2, des2 = sift.detectAndCompute(gray2,None)

# 暴力匹配
bf = cv2.DescriptorMatcher_create(cv2.DescriptorMatcher_BRUTEFORCE)
matches = bf.match(des1,des2)

# 绘制最佳匹配
matches = sorted(matches, key = lambda x:x.distance)
result = cv2.drawMatches(img1, kp1, img2, kp2, matches[:15], None)
cv_show("-match", result)

