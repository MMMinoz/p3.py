class CountList1:
    def __init__(self,*args):
        self.values=[x for x in args]
        print(self.values)
        self.count={}.fromkeys(range(len(self.values)),0)

    def __len__(self):
        return len(self.values)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.values[key]

    
