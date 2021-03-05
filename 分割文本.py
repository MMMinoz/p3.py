f=open('D:\\Python\\test.txt','r')
count=1
boy=[]
girl=[]
def save_file():
    b_n='D:\\Python\\boy'+str(count)+'.txt'
    g_n='D:\\Python\\girl'+str(count)+'.txt'
    f_b=open(b_n,'w')
    f_g=open(g_n,'w')
    f_b.writelines(boy)
    f_g.writelines(girl)
    f_b.close()
    f_g.close()
for each_line in f:
    if each_line[:3]=='===':#保存到boy/girl文件
        save_file()
        count+=1
        boy=[]
        girl=[]
    else:#分割对话
        (role,say)=each_line.split(':',1)
        if role=='boy':
            boy.append(say)
        else:
            girl.append(say)
    
f.close()

for i in range(3):
    b1_n='D:\\Python\\boy'+str(i+1)+'.txt'
    g1_n='D:\\Python\\girl'+str(i+1)+'.txt'
    f1_b=open(b1_n,'r')
    f1_g=open(g1_n,'r')
    for be in f1_b:
        print(be)
    for ge in f1_g:
        print(ge)
    print('\n')
    f1_b.close()
    f1_g.close()
        
