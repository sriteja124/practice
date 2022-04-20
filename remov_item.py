'''class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None

    #inserting an element in the beginning
    def insert_beg(self,Newnode):
        newnode=Node(Newnode)
        newnode.nextval=self.headval
        self.headval=newnode

    #function to remove node
    def removenode(self,key):

        #store headnode
        temp=self.headval

        #if head node itself contains the key which needs to be deleted
        if (temp is not None):
            if (temp.dataval==key):
                self.headval=temp.nextval
                temp=None
                return

        # Search for the key to be deleted
        while (temp is not None):
            if temp.dataval==key:
                break
            prev=temp
            temp=temp.nextval

        #if key was not present in linked list
        if (temp==None):
            return

        #unlike the node from linked list
        prev.nextval=temp.nextval
        temp=None
    #function to print the linkedlist
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
l1.printlist()'''
class Node:
    def __init__(self,dataval):
        self.dataval=dataval
        self.nextval=None
class Linkedlist:
    def __init__(self):
        self.headval=None

    def remove(self,key):
        temp=self.headval
        if (temp is not None):
            if (temp.dataval==key):
                self.headval=temp.nextval
                temp=None

        while (temp is not None):
            if temp.dataval==key:
                break
            prev=temp
            temp=temp.nextval

        if temp==None:
            return

        prev.nextval=temp.nextval
        temp=None

    def printlist(self):
        temp=self.headval
        while temp!=None:
            print(temp.dataval)
            temp=temp.nextval

l1=Linkedlist()
l1.headval=Node("Mon")
l2=Node("Tues")
l3=Node("Wed")
l1.headval.nextval=l2
l2.nextval=l3

l1.remove("Wed")

l1.printlist()