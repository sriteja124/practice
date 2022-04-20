class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None

    def insert_beg(self,Newnode):
        newnode=Node(Newnode)
        newnode.nextval=self.headval
        self.headval=newnode

    #function to remove node
    def removenode(self,key):
        temp=self.headval
        if temp is not None:
            if temp.dataval==key:
                self.headval=temp.nextval
                temp=None
                return
        while (temp is not None):
            if temp.dataval==key:
                break
            prev=temp
            temp=temp.nextval
        if (temp==None):
            return
        prev.nextval=temp.nextval
        temp=None

    def printlist(self):
        temp=self.headval
        while temp is not None:
            print(temp.dataval)
            temp=temp.nextval
l1=Linkedlist()
l1.headval=Node("Tue")
l2=Node("Wed")
l3=Node("Thu")
l1.headval.nextval=l2
l2.nextval=l3
l1.insert_beg("Mon")
l1.removenode("Wed")
l1.printlist()
