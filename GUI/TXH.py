# import tkinter as tk
# root = tk.Tk()
# lb = tk.Label(root,text='第一个标签',\
#            bg='#d3fbfb',\
#            fg='red',\
#            font=('华文新魏',32),\
#            width=20,\
#            relief=tk.SUNKEN)
# lb.pack()
# root.title("hello world")
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
# 1、利用configure更改text
# import tkinter
# import time

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


# 2、textvarible
# import tkinter
# import time
#
# def gettime():
#     var.set(time.strftime("%H:%M:%S"))
#     root.after(1000,gettime)
#
# root = tkinter.Tk()
# root.title('时钟')
# var = tkinter.StringVar()
#
# lb = tkinter.Label(root,textvariable=var,fg='blue',font=('黑体',80))
# lb.pack()
# gettime()
# root.mainloop()

# 文本框某方法
# import tkinter
# import datetime
#
# def gettime():
#     s = str(datetime.datetime.now()) + '\n'
#     text.insert(tkinter.END,s)
#     root.after(1000,gettime)
#
# def deltime():
#     text.delete(0.0)
#
# root = tkinter.Tk()
# root.title('时间')
# root.geometry('320x320')
# text = tkinter.Text(root)
# text.pack()
# gettime()
# deltime()
# root.mainloop()

# #按钮
# #简单的加法器
# import tkinter
#
# def run1():
#     a = float(inp1.get())
#     b = float(inp2.get())
#     s = "{:.2f} + {:.2f} = {:.2f}\n".format(a,b,a+b)
#     txt.insert(tkinter.END,s)
#     inp1.delete(0,tkinter.END)
#     inp2.delete(0,tkinter.END)
#
# def run2(x, y):
#     a = float(x)
#     b = float(y)
#     s = "{:.2f} + {:.2f} = {:.2f}\n".format(a, b, a + b)
#     txt.insert(tkinter.END, s)
#     inp1.delete(0, tkinter.END)
#     inp2.delete(0, tkinter.END)
#
# root = tkinter.Tk()
# root.geometry('460x240')
# root.title('简单的加法器')
#
# lb = tkinter.Label(root, text='请输入两个数，按下面两个按钮之一进行加法计算')
# lb.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.1)
#
# inp1 = tkinter.Entry(root)
# inp1.place(relx=0.1, rely=0.2, relwidth=0.3,relheight=0.1)
# inp2 = tkinter.Entry(root)
# inp2.place(relx=0.6, rely=0.2,relwidth=0.3, relheight=0.1)
#
# #直接调用
# btn1 = tkinter.Button(root, text='方法一', command=run1)
# btn1.place(relx=0.1, rely=0.4, relwidth=0.3, relheight=0.1)
# #使用匿名函数
# btn2 = tkinter.Button(root, text='方法二',command=lambda: run2(inp1.get(),inp2.get()))
# btn2.place(relx=0.6, rely=0.4, relwidth=0.3, relheight=0.1)
#
# txt = tkinter.Text(root)
# txt.place(rely=0.6, relheight=0.4)
#
# root.mainloop()

# #单选
# import tkinter
#
# def Mysel():
#     dic = {1:'甲', 2:'乙', 3:'丙'}
#     s = '您选择了'+dic[var.get()]+'项'
#     lb.config(text=s)
#
# root = tkinter.Tk()
# root.title('单选按钮')
# root.geometry("240x120")
# lb = tkinter.Label(root)
# lb.pack()
#
# #IntVar 是tkinter的一个类，可以管理单选按钮
# #将这三个单选按钮的返回变量都绑定到这个容器上
# var = tkinter.IntVar()
# rd1 = tkinter.Radiobutton(root, text='甲', variable=var, value=1, command=Mysel)
# rd1.pack()
# rd2 = tkinter.Radiobutton(root, text='乙', variable=var, value=2, command=Mysel)
# rd2.pack()
# rd3 = tkinter.Radiobutton(root, text='丙', variable=var, value=3, command=Mysel)
# rd3.pack()
#
# #设置选中的位置，如果越界则全部均不选中
# #有对应的get属性，用来获取选中项的索引
# var.set(0)
# root.mainloop()

# #复选
# import tkinter
#
# def run():
#     if(chvar1.get()==0 and chvar2.get()==0 and chvar3.get()==0 and chvar4.get()==0):
#         s = '您还没有选择任何爱好项目'
#     else:
#         s1 = '足球 ' if chvar1.get() else ''
#         s2 = '篮球 ' if chvar2.get() else ''
#         s3 = '游泳 ' if chvar3.get() else ''
#         s4 = '田径' if chvar4.get() else ''
#         s = '您选择了'+s1+s2+s3+s4
#     lb2.configure(text=s)
#
# root = tkinter.Tk()
# root.geometry('240x240')
# root.title('复选框')
# lb1 = tkinter.Label(root, text='请选择您的爱好项目')
# lb1.pack()
# chvar1 = tkinter.IntVar()
# chvar2 = tkinter.IntVar()
# chvar3 = tkinter.IntVar()
# chvar4 = tkinter.IntVar()
#
# #variable 的值为 1 或 0，代表着选中或不选中
# chvar1.set(1) #默认选中
# ch1 = tkinter.Checkbutton(root, text='足球', variable=chvar1, onvalue=1, offvalue=0)
# ch2 = tkinter.Checkbutton(root, text='篮球', variable=chvar2, onvalue=1, offvalue=0)
# ch3 = tkinter.Checkbutton(root, text='游泳', variable=chvar3, onvalue=1, offvalue=0)
# ch4 = tkinter.Checkbutton(root, text='田径', variable=chvar4, onvalue=1, offvalue=0)
# ch1.pack()
# ch2.pack()
# ch3.pack()
# ch4.pack()
#
# btn = tkinter.Button(root, text='OK', activeforeground='blue', command=run)
# btn.pack()
#
# lb2 = tkinter.Label(root,text='')
# lb2.pack()
#
# root.mainloop()

# import tkinter
#
#
# def init():
#     lstbox1.delete(0, tkinter.END)
#     list_item = ['数学', '物理', '化学', '语文', '外语']
#     for item in list_item:
#         lstbox1.insert(tkinter.END, item)
#
#
# def add():
#     if inp.get() != '':
#         #未指定位置 在末尾插入
#         if lstbox1.curselection() == ():
#             lstbox1.insert(lstbox1.size(), inp.get())
#         #指定位置 在选中的位置上面插入
#         else:
#             lstbox1.insert(lstbox1.curselection(), inp.get())
#
#
# def update():
#     if inp.get() != '' and lstbox1.curselection() != ():
#         selected = lstbox1.curselection()[0]
#         print(type(lstbox1.curselection()))
#         lstbox1.delete(selected)
#         lstbox1.insert(selected, inp.get())
#
#
# def delt():
#     if lstbox1.curselection() != ():
#         lstbox1.delete(lstbox1.curselection())
#
#
# def clear():
#     lstbox1.delete(0, tkinter.END)
#
#
# root = tkinter.Tk()
# root.title('列表框')
# root.geometry('320x240')
#
# frame1 = tkinter.Frame(root, relief=tkinter.RAISED)
# frame1.place(relx=0.0)
# frame2 = tkinter.Frame(root, relief=tkinter.GROOVE)
# frame2.place(relx=0.5)
#
# lstbox1 = tkinter.Listbox(frame1)
# lstbox1.pack()
#
# inp = tkinter.Entry(frame2)
# inp.pack()
#
# btn1 = tkinter.Button(frame2, text='初始化', command=init)
# btn2 = tkinter.Button(frame2, text='插入', command=add)
# btn3 = tkinter.Button(frame2, text='删除', command=delt)
# btn4 = tkinter.Button(frame2, text='更改', command=update)
# btn5 = tkinter.Button(frame2, text='清空', command=clear)
# btn1.pack(fill=tkinter.X)
# btn2.pack(fill=tkinter.X)
# btn3.pack(fill=tkinter.X)
# btn4.pack(fill=tkinter.X)
# btn5.pack(fill=tkinter.X)
#
# root.mainloop()

# #组合框
# import tkinter
# import tkinter.ttk as ttk
#
#
# def calc(event):
#     a = float(inp1.get())
#     b = float(inp2.get())
#     dic = {0: a+b, 1: a-b, 2: a*b, 3: a/b}
#     c = dic[comb.current()]
#     lb.configure(text=str(c))
#
#
# root = tkinter.Tk()
# root.title('组合框')
# root.geometry('320x240')
#
# inp1 = tkinter.Entry(root)
# inp1.place(relx=0.1, rely=0.1, relwidth=0.3, relheight=0.1)
#
# inp2 = ttk.Entry(root)
# inp2.place(relx=0.5, rely=0.1, relwidth=0.3, relheight=0.1)
#
# var = tkinter.StringVar()
#
# comb = ttk.Combobox(root, textvariable=var, values=['加', '减', '乘', '除'])
# comb.place(relx=0.3, rely=0.3, relwidth=0.3, relheight=0.1)
# comb.bind('<<ComboboxSelected>>',calc)
#
# lb = ttk.Label(root, text='结果')
# lb.place(relx=0.3, rely=0.5, relwidth=0.3, relheight=0.1)
# root.mainloop()

# #滑块
# import tkinter
#
#
# def show(event):
#     s = '滑块的取值为' + str(var.get())
#     lb.configure(text=s)
#
#
# root = tkinter.Tk()
# root.title('滑块')
# root.geometry('240x240')
# var = tkinter.DoubleVar()
# scl = tkinter.Scale(root, orient=tkinter.HORIZONTAL, length=200, \
# from_=1.0, to=5.0,label='请拖动滑块', tickinterval=1, resolution=0.05, variable=var)
# scl.bind('<ButtonRelease-1>',show)
# scl.pack()
#
# lb = tkinter.Label(root, text='')
# lb.pack()
#
# root.mainloop()

# 菜单
# import tkinter
#
#
# def new():
#     s = '新建'
#     lb.configure(text=s)
#
#
# def ope():
#     s = '打开'
#     lb.configure(text=s)
#
#
# def sav():
#     s = '保存'
#     lb.configure(text=s)
#
#
# def cut():
#     s = '剪切'
#     lb.configure(text=s)
#
#
# def cop():
#     s = '复制'
#     lb.configure(text=s)
#
#
# def pas():
#     s = '粘贴'
#     lb.configure(text=s)
#
#
# def popupmenu(event):
#     menuPopup.post(event.x_root, event.y_root)
#
#
# root = tkinter.Tk()
# root.title('菜单实验')
# root.geometry('320x240')
#
# lb = tkinter.Label(root, text='显示信息', font=('黑体', 32, 'bold'))
# lb.place(relx=0.2, rely=0.2)
#
# mainmenu = tkinter.Menu(root)
#
# #tearoff=0 / 1 菜单是否能独立出来(虚线)
# menuFile = tkinter.Menu(mainmenu, tearoff=False)
# mainmenu.add_cascade(label='文件', menu=menuFile)
# menuFile.add_command(label='新建', command=new)
# menuFile.add_command(label='打开', command=ope)
# menuFile.add_command(label='保存', command=sav)
# menuFile.add_separator()
# menuFile.add_command(label='退出', command=root.destroy)
#
# menuEdit = tkinter.Menu(mainmenu, tearoff=False)
# mainmenu.add_cascade(label='编辑', menu=menuEdit)
# menuEdit.add_command(label='复制', command=cop)
# menuEdit.add_command(label='剪切', command=cut)
# menuEdit.add_command(label='粘贴', command=pas)
#
# # 绑定鼠标右键
# menuPopup = tkinter.Menu(mainmenu, tearoff=False)
# menuPopup.add_command(label='撤销')
# menuPopup.add_command(label='重做')
#
# root.bind('<Button-3>', popupmenu)
#
# #将root根窗口的顶级菜单设置为 menu
# root.config(menu=mainmenu)
# #root['menu'] = mainmenu 也可以
#
# root.mainloop()

# # 子窗体
# import tkinter
#
# # 弹窗
# def newwind():
#     winnew = tkinter.Toplevel(root)
#     winnew.geometry('240x240')
#     winnew.attributes('-alpha', 0.9)#设置窗口透明度为90%
#     lbb = tkinter.Label(winnew, text='我在新窗体上')
#     lbb.place(relx=0.2, rely=0.2)
#     btclose = tkinter.Button(winnew, text='关闭', command=winnew.destroy)
#     btclose.place(relx=0.3, rely=0.5)
#
#
# root = tkinter.Tk()
# root.title('子窗体')
# root.geometry('240x240')
#
# lb = tkinter.Label(root, text='主窗体', font=('黑体', 32, 'bold'))
# lb.place(relx=0.2, rely=0.2)
#
# mainmenu = tkinter.Menu(root)
# menuFile = tkinter.Menu(mainmenu, tearoff=0)
# mainmenu.add_cascade(label='菜单', menu=menuFile)
# menuFile.add_command(label='新窗体', command=newwind)
# menuFile.add_separator()
# menuFile.add_command(label='退出', command=root.destroy)
#
# root.config(menu=mainmenu)
# root.mainloop()

# #消息对话框
# #文件对话框
# #颜色对话框
# import tkinter
# import tkinter.messagebox
# import tkinter.simpledialog as sim
# import tkinter.filedialog
# import tkinter.colorchooser
#
#
# def dialog():
#     answer = tkinter.messagebox.askokcancel('请选择', '请选择确定或取消')
#     if answer:
#         lb1.config(text='已确认')
#     else:
#         lb1.config(text='已取消')
#
#     s = sim.askstring('请输入', '请输入一串文字')
#     lb2.config(text=s)
#
#     filename = tkinter.filedialog.askopenfilename()
#     if filename != '':
#         lb3.config(text='您选择的文件是'+filename)
#     else:
#         lb3.config(text='您没有选择任何文件')
#
#     color = str(tkinter.colorchooser.askcolor())
#     print('打印字符串%s 切掉后=%s' % (color, color[-9:-2]))
#     lb4.config(text=color[-9:-2], background=color[-9:-2])
#
#
# root = tkinter.Tk()
# root.title('模式对话框')
# root.geometry('240x240')
#
# lb1 = tkinter.Label(root, text='')
# lb1.pack()
# lb2 = tkinter.Label(root, text='')
# lb2.pack()
# lb3 = tkinter.Label(root, text='')
# lb3.pack()
# lb4 = tkinter.Label(root, text='请关注颜色变化')
# lb4.pack()
#
# btn = tkinter.Button(root, text='弹出对话框', command=dialog)
# btn.pack()
#
# root.mainloop()

# import tkinter
# import tkinter.messagebox
#
#
# def show():
#     tkinter.messagebox.askokcancel('show', 'askokcancel')
#     tkinter.messagebox.askquestion('show', 'askquestion')
#     tkinter.messagebox.askretrycancel('show', 'askretrycancel')
#     tkinter.messagebox.askyesno('show', 'askyesno')
#     tkinter.messagebox.showerror('show', 'showerror')
#     tkinter.messagebox.showinfo('show', 'showinfo')
#     tkinter.messagebox.showwarning('show', 'showwarning')
#
# root = tkinter.Tk()
# root.title('模式对话框样式展示')
# root.geometry('240x120')
# lb = tkinter.Label(root, text='')
# lb.pack()
# btn = tkinter.Button(root, text='展示', command=show, width=8)
# btn.pack()
# root.mainloop()


# #事件响应
# import tkinter
#
#
# def keyboard(event):
#     s = event.keysym
#     lb1.config(text=s)
#
# def mouse(event):
#     s='鼠标在(%s,%s)位置' % (event.x, event.y)
#     lb2.config(text=s)
#
#
# root = tkinter.Tk()
# root.title('事件响应')
# root.geometry('500x500')
#
# lb1 = tkinter.Label(root, text='请按键', font=('黑体',30))
# lb1.bind('<Key>',keyboard)
# #接受键盘事件，只有组件获取焦点才能接受键盘事件
# lb1.focus_set()#获取焦点
# lb1.pack()
#
# lb2 = tkinter.Label(root, text='请移动鼠标', font=('黑体', 30))
# root.bind('<Motion>',mouse)
# lb2.pack()
#
# root.mainloop()
