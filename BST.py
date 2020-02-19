class Node:
    def __init__(self):
        self.element=0
        self.leftNode=None
        self.rightNode=None

class BST:
    def __init__(self):
        #self.size=size
        self.tree=None
    def insert(self,element):
        newNode=Node()
        newNode.element=element
        if(self.tree==None):
            self.tree = newNode
        else:
            currentNode=self.tree
            while(currentNode!=None):
                prevNode = currentNode
                if(currentNode.element>element):
                    currentNode=currentNode.leftNode
                elif(currentNode.element<element):
                    currentNode=currentNode.rightNode
            if(prevNode.element>element):
                prevNode.leftNode=newNode
            else:
                prevNode.rightNode=newNode
        return self.tree
    def display(self):
        self.displayTree(self.tree)

    def displayTree(self,Tree):
        if(Tree==None):
            return
        self.displayTree(Tree.leftNode)
        print(Tree.element)
        self.displayTree(Tree.rightNode)
    def levelOrderTraversal(self):
        lst=[]
        currentNode = self.tree
        lst.append(currentNode)
        while(len(lst)>0):
            currentNode=lst[0]
            lst.append(currentNode.leftNode)
            lst.append(currentNode.rightNode)
            print(currentNode.element)
            lst.pop(0)


ch=input("Do u wanna add element to tree? y/n")
tree1=BST()

while(ch=='y'):
    tree1.insert(int(input("Enter the element to add")))
    ch = input("Do u wanna add element to tree? y/n")

print("Level-Order Traversal")
tree1.levelOrderTraversal()



