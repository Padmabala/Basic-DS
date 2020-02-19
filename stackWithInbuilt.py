class stack:
    stk=[]
    def __init__(self,n):
        self.top=-1
        self.n=n
    def push(self,element):
        if(len(self.stk)<self.n):
            self.stk.append(element)
        else:
            print("Stack Full")
    def popElement(self):
        self.stk.pop()
    def display(self):
        for i in range(len(self.stk)):
            print(self.stk[i])
n=int(input("Enter the size of the stack"))
s1=stack(n)
ch=input("Do u want to add element to stack")
while(ch=="y"):
    s1.push(int(input("Enter the element")))
    ch = input("Do u want to add element to stack")
s1.popElement()
s1.display()