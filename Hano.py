def Hano(n):
    if n==1:
        return 1
    return Hano(n-1)*2+1
n=int(input("输入层数n："))
print(Hano(n))
