def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
number=int(input("输入一个整数n:"))
result=factorial(number)
print(result)

