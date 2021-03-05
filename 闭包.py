def myFunc():
    m = 1
    n = 2
    def show():
        print('m的值为:', m)
        nonlocal n #如果不加会报错。
        n += 10
        print('n的值为:', n)
    return show

s = myFunc()
s()
