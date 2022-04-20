class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None
    def printlist(self):
        temp=self.headval
        while temp!=None:
            print(temp.dataval)
            temp=temp.nextval

l1=Linkedlist()
l1.headval=Node("Mon")
l2=Node("Tue")
l3=Node("wed")
l1.headval.nextval=l2
l2.nextval=l3

l1.printlist()