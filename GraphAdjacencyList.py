
class Node:
    def __init__(self,vertex):
        self.element= vertex
        self.next=None
class Graph:
    def __init__(self,graphSize):
        self.graphSize=graphSize
        self.vertices=[]
        self.edges=[]
        self.adjMatrix=[[0]*self.graphSize for x in range(self.graphSize)]
        self.vertD={}
        self.vertexIndex=-1
        self.adjList={}
        self.verticeList=[]
    def addVertex(self,vertex):
        if(len(self.vertices)<self.graphSize):
            self.vertexIndex+=1
            self.vertices.append(vertex)
            self.vertD[vertex]=self.vertexIndex
            self.adjList[vertex]=[]
            n = Node(vertex)
            self.verticeList.append(n)
        else:
            print("Graph full")
    def addEdges(self,v1,v2):
        self.edges.append([v1,v2])
        self.adjMatrix[self.vertD[v1]][self.vertD[v2]]=1
        self.adjMatrix[self.vertD[v2]][self.vertD[v1]] = 1
        self.adjList[self.vertD[v1]]=self.adjList[v1].append(v2)
        temp=self.verticeList[self.vertD[v1]]
        while(temp.next!=None):
            temp=temp.next
        temp.next=Node(v2)

    def displayVertices(self):
        print(self.vertices)
        print(self.vertD)
        print(len(self.verticeList))
        for i in range(len(self.verticeList)):
            print(self.verticeList[i].element)
            print("Edges")
            temp=self.verticeList[i]
            temp=temp.next
            while(temp!=None):
                print(temp.element)
                temp = temp.next
    def displayEdges(self):
        for i in range(self.graphSize):
            for j in range(self.graphSize):
                if(self.adjMatrix[i][j]==1):
                    print(self.vertices[i],self.vertices[j])
    def displayMatrix(self):
        print(self.adjMatrix)
        print(self.adjList)

numOfVertices=int(input("Enter the no . of vertices"))
g=Graph(5)
ch='y'
while(ch=='y'):
    g.addVertex(input("What is the new vertex"))
    ch=input("any more vertices")
ch='y'
while(ch=='y'):
    v1=input("Enter the vertex 1")
    v2=input("Enter the vertex 2")
    g.addEdges(v1,v2)
    ch=input("any more edges")
g.displayEdges()
g.displayMatrix()
g.displayVertices()
