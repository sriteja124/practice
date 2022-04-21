class stack:
    def __init__(self):
        self.stack=[]

    def add(self,val):
        if val not in self.stack:
            self.stack.append(val)
            return True
        else:
            return False

    def peek(self):
        return self.stack[-1]
tack=stack()
tack.add(5)
tack.add(6)
tack.peek()