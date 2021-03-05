from PIL import Image
import numpy as np

# a = np.array(Image.open("cat_500_600.jpg"))
# print(a.shape,a.dtype)
# b = [255,255,255] - a
# im = Image.fromarray(b.astype('uint8'))
# im.save("cat_500_600_2.jpg")
#
# a = np.array(Image.open("cat_500_600.jpg").convert('L'))
# b = 255 - a
# im = Image.fromarray(b.astype('uint8'))
# im.save("cat_500_600_3.jpg")

# a = np.array(Image.open("cat_500_600.jpg").convert('L'))
# c = (100/255)*a + 150 #区间变换
# im = Image.fromarray(c.astype('uint8'))
# im.save("cat_500_600_4.jpg")

# a = np.array(Image.open("cat_500_600.jpg"))
# b = 255 * (a/255)**2 #像素平方
# im = Image.fromarray(b.astype('uint8'))
# im.save("cat_500_600_5.jpg")

a = np.array(Image.open("词云背景2.jpg").convert('L')).astype('float')
depth = 10
grad = np.gradient(a)
grad_x,grad_y = grad
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 +1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A

vec_el = np.pi/2.2
vec_az = np.pi/4
dx = np.cos(vec_el)*np.cos(vec_az)
dy = np.cos(vec_el)*np.sin(vec_az)
dz = np.sin(vec_el)

b = 255*(dx*uni_x + dy * uni_y +dz * uni_z)
b = b.clip(2,255)

im = Image.fromarray(b.astype('uint8'))
im.save("cat_500_600_sh.jpg")
