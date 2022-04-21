class stack:
    def __init__(self):
        self.head=[]

    def add(self,val):
        if val not in self.head:
            self.head.append(val)
            return True
        else:
            return False

    def remove(self):
        return self.head.pop()

tack=stack()
tack.add(4)
tack.add(2)
tack.add(8)
print(tack.head)
print(tack.remove())
