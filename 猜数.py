import random
num = random.randint(1,10)
print("答案是 %d " % num)
guess = int(input("猜数游戏，请输入你猜的数"))
count = 0
while guess != num and count < 3:
    if count == 0:
        if guess > num:
            print("大了大了~")
        else:
            print("小了小了~")
    guess = int(input("猜错了，请重新输入"))
    count = count+1
    if guess == num:
        print("猜对了")
    else:
        if guess > num:
            print("大了大了~")
        else:
            print("小了小了~")
if count == 0:
    print("猜对了")
print("答案是 %d 游戏结束" % num)

