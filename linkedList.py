class node:
    def __init__(self):
        self.element
        self.nextNode=None
class linkedList:
    def __init__(self,n):
        self.n=n
        self.LinkedList=None
    def addElement(self,element):
        newnode = node()
        newnode.element = element
        if(self.LinkedList==None):
            self.LinkedList=newnode
        else:
            while(self.LinkedList.nextNode!=None):
                temp = self.LinkedList.nextNode
            temp.nextNode=newnode




        self.ll[self.position:]=element


