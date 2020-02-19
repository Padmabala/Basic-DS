class stack:
    stk=[]
    def __init__(self,n):
        self.n=n
        self.top=-1

    def push(self,element):
        if(len(self.stk)<self.n):
            self.top=self.top+1
            print(element, self.top, self.n,len(self.stk))
            self.stk[self.top:]=element
        else:
            print("Stack Full")
    def pop(self):
        if(len(self.stk)<0):
            print("Stack Empty")
        else:
            popElement=self.stk[self.top]
            self.top=self.top-1
            return popElement
    def display(self):
        for i in range(self.top+1):
            print(self.stk[i])



arr=[]
s1=stack(5)
ch=input("Do u want to enter element")
while(ch=='y'):
    s1.push(input("Enter the element"))
    ch = input("Do u want to enter element")
s1.pop();
s1.display()



