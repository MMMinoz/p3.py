# import tkinter as tk
# root = tk.Tk()
# lb = tk.Label(root,text='第一个标签',\
#            bg='#d3fbfb',\
#            fg='red',\
#            font=('华文新魏',32),\
#            width=20,\
#            relief=tk.SUNK+
#            .EN)
# lb.pack()
# root.title("hello wrold")
# root.mainloop()

# lb = tk.Label(root,text='Red',fg='Red',relief=tk.GROOVE)
# lb.pack()
# lb = tk.Label(root,text='绿色',fg='green',relief=tk.GROOVE)
# lb.pack(side=tk.LEFT)
# lb=tk.Label(root,text='蓝',fg='blue',relief=tk.GROOVE)
# lb.pack(fill=tk.X)
# root.mainloop()

# lb = tk.Label(root,text='Red',fg='Red',relief=tk.GROOVE)
# lb.grid(column=2,row=0)
# lb = tk.Label(root,text='绿色',fg='green',relief=tk.GROOVE)
# lb.grid(column=0,row=1)
# lb = tk.Label(root,text='蓝',fg='blue',relief=tk.GROOVE)
# lb.grid(column=1,row=2,columnspan=2,ipadx=20)
# lb.mainloop()

# root.geometry('320x240')
# msg1 = tk.Message(root,text='我的水平起始位置相对于窗体0.2 ，垂直起始位置为绝对位置80像素')
# msg1.place(relx=0.2,y=80,relheight=0.4,width=200)
# root.mainloop()

# #时钟
# #1、利用configure更改text
# import tkinter
# import time
#
# def gettime():
#     timestr = time.strftime('%H:%M:%S')
#     lb.configure(text=timestr)#重新设置text文本
#     root.after(1000,gettime)
#
# root = tkinter.Tk()
# root.title('时钟')
#
# lb = tkinter.Label(root,text='',fg='blue',font=('黑体',80))
# lb.pack()
# gettime()
# root.mainloop()

#2、textvarible
import tkinter
import time

def gettime():
    var.set(time.strftime("%H:%M:%S"))
    root.after(1000,gettime)

root = tkinter.Tk()
root.title('时钟')
var = tkinter.StringVar()

lb = tkinter.Label(root,textvariable=var,fg='blue',font=('黑体',80))
lb.pack()
gettime()
root.mainloop()
