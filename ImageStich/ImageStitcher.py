from Stitcher import Stitcher
import cv2


class ImageStiching:

    def imageStiching(self, img1, img2):
        # 读取拼接图片
        imageA = cv2.imread(img1)
        imageB = cv2.imread(img2)
        # cv2.imshow("Image A", imageA)
        # cv2.imshow("Image B", imageB)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # 把图片拼接起来
        stitcher = Stitcher()
        stitcher.stitch([imageA, imageB])

