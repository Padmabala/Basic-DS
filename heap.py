class Heap:
    def __init__(self):
        self.heapDS=[]
        self.currentHeapIndex=-1
    def insertIntoMinHeap(self,element):
        self.currentHeapIndex+=1
        self.heapDS.append(element)
        self.percUpMinHeapify(self.currentHeapIndex)
    def percUpMinHeapify(self,currentEleIndex):
        parentIndex=self.getParent(currentEleIndex)
        if(parentIndex<0 or self.heapDS[currentEleIndex] > self.heapDS[parentIndex]):
            return
        else:
            self.swap(currentEleIndex, parentIndex)
            currentEleIndex = parentIndex
            self.percUpMinHeapify(currentEleIndex)
    def insertIntoMaxHeap(self,element):
        self.currentHeapIndex += 1
        self.heapDS.append(element)
        self.percUpMaxHeapify(self.currentHeapIndex)

    def percUpMaxHeapify(self, currentEleIndex):
        parentIndex = self.getParent(currentEleIndex)
        if (parentIndex < 0 or self.heapDS[currentEleIndex] < self.heapDS[parentIndex]):
            return
        else:
            self.swap(currentEleIndex, parentIndex)
            currentEleIndex = parentIndex
            self.percUpMaxHeapify(currentEleIndex)
    def delte(self):
        rootIndex=0
        print(self.heapDS[rootIndex]," element has been deleted")
        self.heapDS[rootIndex]=self.heapDS[self.currentHeapIndex]
        self.currentHeapIndex-=1
        self.heapDS.pop()
        self.percDownMaxHeapify(rootIndex)
    def percDownMinHeapify(self,rootIndex):
        if(rootIndex>self.currentHeapIndex):
            return
        leftChild = self.getLeftChild(rootIndex)
        rightChild = self.getRightChild(rootIndex)
        if(leftChild<self.currentHeapIndex or rightChild<self.currentHeapIndex):
            minChild = self.min(leftChild, rightChild)
            if(self.heapDS[minChild]<self.heapDS[rootIndex]):
                self.swap(minChild,rootIndex)
                rootIndex=minChild
                self.percDownMinHeapify(rootIndex)
            else:
                return
        else:
            return
    def percDownMaxHeapify(self,rootIndex):
        if(rootIndex>self.currentHeapIndex):
            return
        leftChild = self.getLeftChild(rootIndex)
        rightChild = self.getRightChild(rootIndex)
        if(leftChild<self.currentHeapIndex or rightChild<self.currentHeapIndex):
            maxChild = self.max(leftChild, rightChild)
            if(self.heapDS[maxChild]>self.heapDS[rootIndex]):
                self.swap(maxChild,rootIndex)
                rootIndex=maxChild
                self.percDownMinHeapify(rootIndex)
            else:
                return
        else:
            return
    def getLeftChild(self,root):
        return ((2*root)+1)
    def getRightChild(self,root):
        return ((2*root)+2)
    def getParent(self,currentIndex):
        return ((currentIndex-1)//2)
    def swap(self,currentIndex,parentIndex):
        self.heapDS[currentIndex],self.heapDS[parentIndex]=self.heapDS[parentIndex],self.heapDS[currentIndex]
    def min(self,leftChild,rightChild):
        if(self.heapDS[leftChild]<self.heapDS[rightChild]):
            return leftChild
        else:
            return rightChild
    def max(self,leftChild,rightChild):
        if(self.heapDS[leftChild]>self.heapDS[rightChild]):
            return leftChild
        else:
            return rightChild
    def display(self):
        print(self.heapDS)




h1=Heap()
ch='y'
while(ch=='y'):
    h1.insertIntoMaxHeap(int(input("Enter the element")))
    ch=input("any more elements")
h1.display();
h1.delte();
h1.display();
