# r 只读模式，若文件不存在返回FileNotFoundError
# w 覆盖写模式，文件不存在则创建，存在则完全覆盖
# x 创建写模式 文件不存在则创建，存在则返回FileExistsError
# a 追加写模式，文件不存在则创建，存在则在文件最后追加内容
# b 二进制文件模式
# t 文本文件模式，默认值
# + 与r/w/x/a同时使用，在原功能基础上增加同时读写功能
# f.read(size)读取全文，如果给出参数size，则滴入前size长度
# f.readline()读取一行
# f.readlines(hint)读入前hint行(当hint=-1时，读入所有行)，以每行为元素形成列表
# f.write(s) 向文件中写入s
# f.writelines(lines)将一个元素全为字符串的列表写入文件(没有换行空格d的直接拼接)
# f.seek(offset) 改变当前文件操作指针的位置，offset：0文件开头，1当前位置 2 文件结尾

# #一次读入
# f = open("output","r")
# txt = f.read()
# ...
# f.close()
#
# #按数量读入,一次读k长度
# f = open("output","r")
# txt = f.read(k)
# ...
# f.close()
#
# #分行读入
# f = open("output","r")
# for line in f.readlines():
#     ...
# f.close()


# import turtle as t
# t.title("自动轨迹绘制")
# t.setup(800,600,0,0)
# t.pencolor("red")
# t.pensize(5)
#
# datals = []
# f = open("data.txt")
# for line in f:
#     line = line.replace("\n","")
#     datals.append(list(map(eval,line.split(","))))
# f.close()
# t.penup()
# t.goto(-200,-200)
# t.pendown()
# for i in range(len(datals)):
#     t.pencolor(datals[i][3],datals[i][4],datals[i][5])
#     t.fd(datals[i][0])
#     if datals[i][1]:
#         t.right(datals[i][2])
#     else:
#         t.left(datals[i][2])
# t.done()
#
# fo = open(name)
# ls = []
# for line in fo:
#     line = line.replace("\n",'')
#     ls.append(line.split(","))
# fo.close()
#
# ls = [[],[],[]]
# f = open(fnme,'w')
# for item in ls:
#     f.write(','.join(itme) + '\n')
# f.close()

#wordcloud

import wordcloud
import jieba
#width,height图片宽度高度
#min_font_size指定词云中现实的最大字号(出现次数最少的用最小字号)
#max_font_size指定词云中现实的最大字号
#指定词云中字体字号的步进间隔，默认为1
#指定字体文件的路径(即改变字体)，默认None
#max_words指定词云中显示的最大单词数,默认200
#指定词云中排除词列表,即不显示的单词列表
#mask指定词云图片形状
#background_color指定词云背景颜色 默认黑
w = wordcloud.WordCloud(background_color="white")
#向WordCloud对象w中加载文本txt
txt1 = "life is short,you need python"
w.generate(txt1)
#将词云输出为图像文件png/jpg
w.to_file("pywordcloud.jpg")

txt2 = "程序设计语言时计算机能够理解和 \
       识别用户操作意图的一种交互体系，他按照\
       特定的规则组织计算机指令，使计算机 \
       能够自动进行各种运算处理"
w = wordcloud.WordCloud(width=1000,font_path="msyh.ttc",height=700)
w.generate(" ".join(jieba.lcut(txt2)))
w.to_file("Chipywordcloud.jpg")


# import jieba
# import wordcloud
# import imageio
#
# mask = imageio.imread("词云背景.jpg")
# f = open("词云test.txt","r",encoding="utf-8")
# t = f.read()
# f.close()
#
# w = wordcloud.WordCloud(background_color="white",
#                         font_path="msyh.ttc",
#                         max_words=100,mask=mask)
# w.generate(" ".join(jieba.lcut(t)))
# w.to_file("词云test.jpg")

