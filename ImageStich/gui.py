import tkinter
from ImageStitcher import ImageStiching
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk


# 图片缩放
def resize(w, h, w_box, h_box, img):
    f1 = 1.0 * w_box / w
    f2 = 1.0 * h_box / h
    factor = min(f1, f2)
    width = int(w * factor)
    height = int(h * factor)
    return img.resize((width, height), Image.ANTIALIAS)


# 图片类型转换
def transform(img, width, height):
    img = Image.open(img)
    w, h = img.size
    img = resize(w, h, width, height, img)
    img = ImageTk.PhotoImage(img)
    return img


# 得到图片1地址并显示
def choosepic1():
    global img1
    img1 = askopenfilename()
    img = transform(img1, 200, 200)
    lb1.configure(image=img)
    lb1.image = img


# 得到图片2地址并显示
def choosepic2():
    global img2
    img2 = askopenfilename()
    img = transform(img2, 200, 200)
    lb2.configure(image=img)
    lb2.image = img


# 标签
def labelShow():
    # 灰度图
    lb3 = tkinter.Label(canvas, text='灰度图', bg='white', fg='Blue3', font=('黑体', 13))
    lb3.place(relx=0.6, rely=0.03)
    # 特征点图
    lb4 = tkinter.Label(canvas, text='特征点图', bg='white', fg='Blue3', font=('黑体', 13))
    lb4.place(relx=0.815, rely=0.03)
    # 匹配图
    lb5 = tkinter.Label(canvas, text='匹配线', bg='white', fg='Blue3', font=('黑体', 13))
    lb5.place(relx=0.15, rely=0.65)
    # 连接图
    lb6 = tkinter.Label(canvas, text='拼接图', bg='white', fg='Blue3', font=('黑体', 13))
    lb6.place(relx=0.45, rely=0.65)
    # 结果图
    lb7 = tkinter.Label(canvas, text='结果图', bg='white', fg='Blue3', font=('黑体', 13))
    lb7.place(relx=0.78, rely=0.65)

# 展示结果图
def showresult():
    global gray1
    gray1 = transform('gray1.png', 200, 200)
    canvas.create_image(700, 150, image=gray1)
    global gray2
    gray2 = transform('gray2.png', 200, 200)
    canvas.create_image(700, 350, image=gray2)
    global sift1
    sift1 = transform('sift1.png', 200, 200)
    canvas.create_image(950, 150, image=sift1)
    global sift2
    sift2 = transform('sift2.png', 200, 200)
    canvas.create_image(950, 350, image=sift2)
    global vis
    vis = transform('vis.png', 300, 300)
    canvas.create_image(200, 680, image=vis)
    global rresult
    rresult = transform('rresult.png', 300, 300)
    canvas.create_image(550, 680, image=rresult)
    global result
    result = transform('result.png', 300, 300)
    canvas.create_image(900, 680, image=result)


# 图像拼接
def resultimg():
    global img1, img2
    Test = ImageStiching()
    Test.imageStiching(img1, img2)
    showresult()


root = tkinter.Tk()
root.title('图像拼接')
root.geometry('1100x1000')
canvas = tkinter.Canvas(root, bg='white', height=1000, width=1100)

lb1 = tkinter.Label(canvas)
lb2 = tkinter.Label(canvas)
lb1.place(relx=0.15, rely=0.03, width=200, height=200)
lb2.place(relx=0.15, rely=0.28, width=200, height=200)

btn1 = tkinter.Button(canvas, text='选择图片', bg='lavender', fg='blue', font=('黑体', 13),
                      relief=tkinter.RAISED, command=choosepic1)
btn1.place(relx=0.03, rely=0.13, relwidth=0.08, relheight=0.04)

btn2 = tkinter.Button(canvas, text='确定', bg='lavender', fg='blue', font=('黑体', 13))
btn2.place(relx=0.37, rely=0.13, relwidth=0.08, relheight=0.04)

btn3 = tkinter.Button(canvas, text='选择图片', bg='lavender', fg='blue', font=('黑体', 13),
                      relief=tkinter.RAISED, command=choosepic2)
btn3.place(relx=0.03, rely=0.38, relwidth=0.08, relheight=0.04)

btn4 = tkinter.Button(canvas, text='确定', bg='lavender', fg='blue', font=('黑体', 13))
btn4.place(relx=0.37, rely=0.38, relwidth=0.08, relheight=0.04)

btn5 = tkinter.Button(canvas, text='结  果', bg='lavender', fg='blue',
                      font=('黑体', 13), command=resultimg)
btn5.place(relx=0.48, rely=0.55, relwidth=0.1, relheight=0.05)

labelShow()

canvas.pack()
root.mainloop()
