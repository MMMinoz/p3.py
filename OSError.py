try:
    sum=1+'1'
    f=open("mm.txt")
    print(f.read())
    f.close()
#except OSError as reason:
#	print('文件出错了，错误原因是'+str(reason))
#except TypeError as reason:
#    print('类型错误'+str(reason))
except (OSError,TypeError):
    print('出错了')

