class Graph:
    def __init__(self,size):
        self.vertexList={}
        self.vertexIndex=0
        self.adjList={}
        self.size=size
        for i in range(size):
            self.adjList[i]=[]
    def addEdge(self,v1,v2):
        if(v1==v2):
            print("%d and %d are the same",(v1,v2))
        else:
            if(v1 in self.vertexList):
                self.adjList[self.vertexList[v1]].append(v2)
            else:
                self.vertexList[v1]=self.vertexIndex
                self.vertexIndex=self.vertexIndex+1
                self.adjList[self.vertexList[v1]].append(v2)
    def removeEdge(self,v1,v2):
        if v2 not in self.adjList[self.vertexList[v1]]:
            print("%d not in adjacency list of %d", (v1, v2))
            return
        self.adjList[self.vertexList[v1]].remove(v2)
    def contains(self,v1,v2):
        return True if v2 in self.adjList[self.vertexList[v1]] else False
    def toString(self):
        for key,value in self.vertexList.items():
            print(key,"to ",self.adjList[value])
def main():
    g = Graph(5)
    g.addEdge('bihar','china')
    g.addEdge('china','usa')
    g.toString()
    g.removeEdge('bihar','china')
    g.toString()
if __name__=='__main__':
    main()
