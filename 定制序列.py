class CountList2:
    def __init__(self,*args):
        self.values=[x for x in args]
        self.count = dict.fromkeys(self.values, 0)
        print(self.count)

    def __len__(self):
        return len(self.count)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.count[key]

    def __setitem__(self,key,value):
        self.count[key]+=1
        super().__setitem__(key,value)
    
    def __delitem__(self,key):
        self.count.pop(key)
        super().__delitem__(key)
