def Fab(n):
    if n==1 or n==2:
        return 1
    return Fab(n-1)+Fab(n-2)
num=int(input("输入n:"))
print(Fab(num))
