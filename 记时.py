import time as t

class MyTimer():

    def __init__(self):
        self.num=['年','月','天','小时','分钟','秒']
        self.prompt="未开始计时!"
        self.lasted=[]
        self.begin=0
        self.end=0

    def __str__(self):
        return self.prompt

    __repr__=__str__

    
    def start(self):
        self.begin=t.localtime()
        self.prompt="请先调用stop()停止计时！"
        print("计时开始...")

    def stop(self):
        if not self.begin:
            print("请先调用start()开始计时!")
        else:
            self.end=t.localtime();
            self._calc()
            print("计时结束...")

    def _calc(self):
        self.lasted=[]
        self.prompt="总共运行了"
        for index in range(6):
            self.lasted.append(self.end[index]-self.begin[index])
        print(self.lasted)
        
        for index in range(5,-1,-1):
            if self.lasted[index]<0:
                self.lasted[index]+=60
                self.lasted[index-1]-=1
        for index in range(6):
            print(self.lasted[index])
            if self.lasted[index]:
                self.prompt+=(str(self.lasted[index])+self.num[index])
        
        self.begin=0
        self.end=0

