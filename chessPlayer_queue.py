class queue:
    def __init__(self):
        self.store=[]
    def enqueue(self,value):
        self.store=[value]+self.store
        return True
    def dequeue(self):
        if (len(self.store)<=0):
            return [False,0]
        r=self.store[len(self.store)-1]
        self.store=self.store[0:len(self.store)-1]
        return [True,r]
    def isEmpty(self):
        if (len(self.store)<=0):
            return True
        return False