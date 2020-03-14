class Graph:
    def __init__(self,size):
        self.adjList={}
        self.size=size
        for i in range(size):
            self.adjList[i]=[]
    def addEdge(self,v1,v2):
        if(v1==v2):
            print("%d and %d are the same",(v1,v2))
        else:
            if v2 not in self.adjList[v1]:
                self.adjList[v1].append(v2)
    def removeEdge(self,v1,v2):
        if v2 not in self.adjList[v1]:
            print("%d not in adjacency list of %d", (v1, v2))
            return
        self.adjList[v1].remove(v2)
    def contains(self,v1,v2):
        return True if v2 in self.adjList[v1] else False
    def toString(self):
        for key,value in self.adjList.items():
            print(key,"to ",value)
def main():
    g = Graph(5)
    g.addEdge(0,1)
    g.addEdge(1,2)
    g.addEdge(1,3)
    g.addEdge(0,4)
    g.toString()
    g.removeEdge(0,4)
    g.toString()
if __name__=='__main__':
    main()
