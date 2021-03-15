from Stitcher import Stitcher
import cv2

#读取拼接图片
imageA = cv2.imread('left_01.png')
imageB = cv2.imread('right_01.png')
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 把图片拼接起来
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB])

# 显示图片
cv2.imshow("Keypoint Matches", vis)
cv2.waitKey(0)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()