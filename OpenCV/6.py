import cv2
import matplotlib.pyplot as plt
import numpy as np

def cv_show(name, img):
    cv2.imshow(name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# img = cv2.imread('1.jpg')
# cv_show('img',img)
# hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# #plt版
# #img.ravel()是降维后的一维数组，用直方图表达
# plt.hist(img.ravel(), bins=256, rwidth=0.8)
# plt.show()
# #opencv版
# #hist返回每个像素块在图像中的数量，用坐标系表达直方图
# plt.plot(hist)
# plt.show()
#
# img = cv2.imread('1.jpg')
# color = ('b', 'g', 'r')
# for i, col in enumerate(color):
#     histr = cv2.calcHist([img], [i], None, [256], [0, 256])
#     plt.plot(histr,color=col)
#     plt.xlim([0,256])
# plt.show()
#
# #mask
# img = cv2.imread('1.jpg')
# mask = np.zeros(img.shape[:2],np.uint8)
# mask[30:80,30:80] = 255
# cv_show('img',mask)
# masked_img = cv2.bitwise_and(img,img,mask=mask)
# cv_show('img',masked_img)
# hist_full = cv2.calcHist([img],[0],None,[256],[0,256])
# hist_mask = cv2.calcHist([img],[0],mask,[256],[0,256])
#
# plt.subplot(221),plt.imshow(img,'gray')
# plt.subplot(222),plt.imshow(mask,'gray')
# plt.subplot(223),plt.imshow(masked_img,'gray')
# plt.subplot(224),plt.plot(hist_full),plt.plot(hist_mask)
# plt.show()
#
# # #直方图均衡化
# img = cv2.imread('1.jpg',0)
# equ = cv2.equalizeHist(img)
# plt.hist(equ.ravel(), bins=256, rwidth=2)
# plt.show()
# cv_show('equ', equ)
# #
# #自适应直方图均衡化
# clahe = cv2.createCLAHE(clipLimit=2.0 ,tileGridSize=(8,8))
# res_clahe = clahe.apply(img)
# res = np.hstack((img,equ,res_clahe))
# cv_show('res',res)


# #滤波
# img = cv2.imread('lena.jpg', 0)
# img_float32 = np.float32(img)
# dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
# #得到灰度图能表示的形式
# magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
#
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(magnitude_spectrum, cmap='gray')
# plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
# plt.show()

# #低通滤波
# img = cv2.imread('lena.jpg',0)
# img_float32 = np.float32(img)
# #进行傅里叶变化
# dft = cv2.dft(img_float32,flags=cv2.DFT_COMPLEX_OUTPUT)
# #将图像中的低频部分移动到图像的中心
# dft_shift = np.fft.fftshift(dft)
#
# #中心位置
# row, cols = img.shape
# crow, ccol = int(row/2), int(cols/2)
#
# #低通滤波
# mask = np.zeros((row, cols, 2),np.uint8)
# mask[crow-30:crow+30,ccol-30:ccol+30] = 1
#
# fshift = dft_shift*mask
# #进图像的低频和高频部分移动到图像原来的位置
# f_ishift = np.fft.ifftshift(fshift)
# #进行傅里叶的逆变化
# img_back = cv2.idft(f_ishift)
# #将sqrt(x^2 + y^2) 计算矩阵维度的平方根
# img_back = cv2.magnitude(img_back[:, :, 0],img_back[:, :,1])
#
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img_back, cmap='gray')
# plt.title('Result'), plt.xticks([]), plt.yticks([])
# plt.show()

# #高通滤波
# img = cv2.imread('lena.jpg', 0)
# img_float32 = np.float32(img)
# dft = cv2.dft(img_float32, flags=cv2.DFT_COMPLEX_OUTPUT)
# dft_shift = np.fft.fftshift(dft)
#
# # 中心位置
# row, cols = img.shape
# crow, ccol = int(row / 2), int(cols / 2)
#
# # 高通滤波
# mask = np.ones((row, cols, 2), np.uint8)
# # 所以计算图像长宽是为制作mask,中心(30+30)x(30x30)区域为1
# mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 0
#
# fshift = dft_shift * mask
# f_ishift = np.fft.ifftshift(fshift)
# img_back = cv2.idft(f_ishift)
# img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])
#
# plt.subplot(121), plt.imshow(img, cmap='gray')
# plt.title('Input Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122), plt.imshow(img_back, cmap='gray')
# plt.title('Result'), plt.xticks([]), plt.yticks([])
# plt.show()
a = np.random.randint(0, 6, (1, 1, 2))
print(a.shape)
print(a)
b, c = a.ravel()
print(b,c)
