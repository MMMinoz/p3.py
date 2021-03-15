import numpy as np
import cv2


class Stitcher:

    # 拼接函数
    def stitch(self, images, ratio=0.75, reprojThresh=4.0):
        # 获取输入图片
        (imageB, imageA) = images
        # 检测A、B图片的SIFT关键特征点，并计算特征描述子
        # 关键点 特征点
        (kpsB, featuresB) = self.detect_describe(imageB, 1)
        (kpsA, featuresA) = self.detect_describe(imageA, 2)

        # 匹配两张图片的所有特征点，返回匹配结果
        M = self.match_keypoints(kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh)

        # 如果返回结果为空，没有匹配成功的特征点，退出算法
        if M is None:
            return None

        # 否则，提取匹配结果
        # H是3x3视角变换矩阵      
        (matches, H, status) = M
        # 将图片A进行视角变换变形，result是变换后图片
        # imageA：输入的图像
        # H：透视变换的矩阵
        # shape，大小
        result = cv2.warpPerspective(imageA, H, (imageA.shape[1] + imageB.shape[1], imageA.shape[0]))
        # self.cv_show('result', result)
        cv2.imwrite('rresult.png', result)
        # 将图片B传入result图片最左端
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB
        # self.cv_show('result', result)
        cv2.imwrite('result.png', result)


        # vis是连线匹配图 result是结果图
        vis = self.draw_matches(imageA, imageB, kpsA, kpsB, matches, status)
        cv2.imwrite('vis.png', vis)

    # 显示图片
    def cv_show(self, name, img):
        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    # 显示灰度图
    def cv_gray(self, image, index):
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('gray', gray)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        name = 'gray' + str(index) + '.png'
        cv2.imwrite(name, gray)
        return gray


    def draw(self, gray, kps, index):
        # 绘制特征点
        sift_img = cv2.drawKeypoints(gray, kps, gray)
        # cv2.imshow('img', sift_img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()
        name = 'sift' + str(index) + '.png'
        cv2.imwrite(name, sift_img)
        return sift_img

    # sift特征值匹配绘制
    def detect_describe(self, image, index):
        # 将彩色图片转换成灰度图
        gray = self.cv_gray(image, index)
        # 建立SIFT生成器
        descriptor = cv2.xfeatures2d.SIFT_create()

        # 检测SIFT特征点，并计算特征描述符
        # kps是关键点。它所包含的信息有：
        # angle：角度，表示关键点的方向，为了保证方向不变形，SIFT算法通过对关键点周围邻域进行梯度运算，求得该点方向。-1为初值。
        # class_id：当要对图片进行分类时，我们可以用class_id对每个特征点进行区分，未设定时为 - 1，需要靠自己设定
        # octave：代表是从金字塔哪一层提取的得到的数据。
        # pt：关键点点的坐标
        # response：响应程度，代表该点强壮大小，更确切的说，是该点角点的程度。
        # size：该点直径的大小
        (kps, features) = descriptor.detectAndCompute(image, None)

        # 绘制特征点
        self.draw(gray, kps, index)

        # 将结果转换成NumPy数组, pt是元组 tuple 指关键点的坐标
        kps = np.float32([kp.pt for kp in kps])

        # 返回特征点集，及对应的描述特征
        return (kps, features)

    # 暴力匹配
    def match_keypoints(self, kpsA, kpsB, featuresA, featuresB, ratio, reprojThresh):
        # 建立暴力匹配器
        matcher = cv2.BFMatcher()

        # 使用KNN检测来自A、B图的SIFT特征匹配对，K邻近个，这里选K=2
        # Knnmatch返回的两个DMatch类型：是两个与原图像特征点最接近的俩个特征点
        # DMach类型,包括queryIdx,trainIdx,distance
        # queryIdx：测试图像的特征点描述符的下标（第几个特征点描述符），同时也是描述符对应特征点的下标。
        # trainIdx：样本图像的特征点描述符下标, 同时也是描述符对应特征点的下标。
        # distance：代表匹配的特征点描述符的欧式距离，数值越小也就说明俩个特征点越相近。
        rawMatches = matcher.knnMatch(featuresA, featuresB, 2)

        matches = []
        for m in rawMatches:
            # 当最近距离跟次近距离的比值小于ratio值时，保留此匹配对
            ptsA = []
            ptsB = []
            if len(m) == 2 and m[0].distance < m[1].distance * ratio:
                # 存储两个点在featuresA, featuresB中的索引值
                matches.append((m[0].trainIdx, m[0].queryIdx))
                ptsA.append(np.float32(kpsA[m[0].trainIdx]))

        # 当筛选后的匹配对大于4时，计算视角变换矩阵
        # 3x3矩阵 需要8个方程，4对(x,y)
        if len(matches) > 4:
            # 获取匹配对的点坐标
            ptsA = np.float32([kpsA[i] for (_, i) in matches])
            ptsB = np.float32([kpsB[i] for (i, _) in matches])

            # 计算视角变换矩阵 使用RANSAC方法
            # ptsA, pts是两视图中匹配的点
            # method是计算单应矩阵所使用的方法，是一个枚举值。
            # reprojThresh是允许的最大反投影错误，只在使用RANSAC方法时有效。
            (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC, reprojThresh)

            # 返回结果
            return (matches, H, status)

        # 如果匹配对小于4时，返回None
        return None

    # 根据匹配连接
    def draw_matches(self, imageA, imageB, kpsA, kpsB, matches, status):
        # 初始化可视化图片，将A、B图左右连接到一起
        (hA, wA) = imageA.shape[:-1]
        (hB, wB) = imageB.shape[:-1]

        # 生成一个三位数组，维度为max(hA, hB) * (wA + wB) * 3
        vis = np.zeros((max(hA, hB), wA + wB, 3), dtype="uint8")

        vis[0:hA, 0:wA] = imageA
        vis[0:hB, wA:] = imageB

        # 联合遍历，画出匹配对
        for ((trainIdx, queryIdx), s) in zip(matches, status):
            # 当点对匹配成功时，画到可视化图上
            if s == 1:
                # 画出匹配对
                ptA = (int(kpsA[queryIdx][0]), int(kpsA[queryIdx][1]))
                ptB = (int(kpsB[trainIdx][0]) + wA, int(kpsB[trainIdx][1]))
                cv2.line(vis, ptA, ptB, (0, 255, 0), 1)

        # 返回可视化结果
        return vis
