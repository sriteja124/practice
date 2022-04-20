class Node:
    def __init__(self,data):
        self.data=data
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headvalue=None

    def printthings(self):
        val = self.headvalue
        while val is not None:
            print(val.data)
            val = val.nextval
    def atbeg(self,newdata):
        l4=Node(newdata)
        l4.nextval=self.headvalue
        self.headvalue=l4
l1=Linkedlist()
l1.headvalue=Node("Mon")
l2=Node("Tues")
l3=Node("Wed")
l1.headvalue.nextval=l2
l2.nextval=l3

l1.atbeg("Thu")
l1.printthings()