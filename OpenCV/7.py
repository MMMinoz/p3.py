import cv2
import numpy as np

# # 背景建模
# cap = cv2.VideoCapture('test.avi')
# #构造一个特定大小和形状的结构元素，用于图像形态学处理
# kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
# #创建混合高斯模型用于背景建模
# fgbg = cv2.createBackgroundSubtractorMOG2()
#
# while(True):
#     ret,frame = cap.read()
#     fgmask = fgbg.apply(frame)
#     #形态学开运算去噪点
#     fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)
#     #寻找视频中的轮廓
#     im, contours, heirarchy = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
#     for c in contours:
#         #计算各轮廓的周长
#         perimeter = cv2.arcLength(c, True)
#         if perimeter > 188:
#             #找到一个直矩形(不会旋转)
#             x, y, w, h = cv2.boundingRect(c)
#             #画出这个矩形
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,2), 2)
#
#     cv2.imshow('frame', frame)
#     cv2.imshow('fgmask', fgmask)
#     k = cv2.waitKey(100) & 0xff
#     if k == 27:#退出键
#         break
#
# cap.release()
# cv2.destroyAllWindows()

# 光流估计
cap = cv2.VideoCapture('test.avi')

#角点检测所需参数
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7)

#lucas kanade参数
lk_params = dict(winSize=(15, 15), maxLevel=2)

#随机颜色条
color = np.random.randint(0, 255, (100, 3))

#拿到第一帧图像
ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
#退回所有检测特征点，需要输入图像，角点最大数量(效率)，品质因子(特征值越大的越好，来筛选)
#距离相当于这个区间有比这个角点强的，就不要这个弱的了

p0 = cv2.goodFeaturesToTrack(old_gray, mask=None, **feature_params)

#创建一个mask
mask = np.zeros_like(old_frame)

while(True):
    ret, frame = cap.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #需要传入前一帧和当前图像以及前一帧检测到的角点
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)

    #st=1表示
    good_new = p1[st == 1]
    good_old = p0[st == 1]

    # #绘制轨迹
    # for i, (new, old) in enumerate(zip(good_new, good_old)):
    #     a, b = new.ravel()
    #     c, d = old.ravel()
    #     mask = cv2.line(mask, (a, b), (c, d), color[i].tolist(), 2)
    #     frame = cv2.circle(frame, (a, b), 5, color[i].tolist(), -1)
    #绘制轨迹
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a = new.ravel()
        b = old.ravel()
        mask = cv2.line(mask, tuple(a), tuple(b), color[i].tolist(), 2)
        frame = cv2.circle(frame, tuple(a), 5, color[i].tolist(), -1)
    img = cv2.add(frame, mask)

    cv2.imshow('frame', img)
    k = cv2.waitKey(150) & 0xff
    if k == 27:
        break

    #更新
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1,2)

cap.release()
cv2.destroyAllWindows()