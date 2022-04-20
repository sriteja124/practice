class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None

    def insert_betw(self,middlenode,newnode):
        if middlenode is None:
            print("The mentioned node is absent")
            return
        Newnode=Node(newnode)
        Newnode.nextval=middlenode.nextval
        middlenode.nextval=Newnode

    def printlist(self):
        temp=self.headval
        while temp is not None:
            print(temp.dataval)
            temp=temp.nextval

l1=Linkedlist()
l1.headval=Node("Mon")
l2=Node("Tues")
l3=Node("Thu")
l1.headval.nextval=l2
l2.nextval=l3
l1.insert_betw(l1.headval.nextval,"Wed")

l1.printlist()