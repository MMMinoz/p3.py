class rectangle:
    def __init__(self,width=0,height=0):
        self.w=width
        self.h=height
        self.name=5
        
    def __setattr__(self,name,value):
        self.name=value
        self.w=value
        self.h=value
        else:
            #__setarrt__本质就是用__dict__进行赋值
            super().__setattr__(name,value)
            self.__dict__[name]=value 

    def getArea(self):
        return self.w*self.h
 
