class Graph:
    def __init__(self,size):
        #self.adjMatrix={[]for i in range(size)}
        # for i in range(size):
        #     self.adjMatrix.append([0 for i in range(size)])
        self.adjList={}
        self.vCount=0
        self.adjMatrix = {}
        for i in range(size):
            self.adjMatrix[i] = []
        #self.adjMatrix[0].append(1)
        #self.adjMatrix[0].append(2)
        self.size=size

    def addEdge(self,v1,v2):
        if(v1==v2):
            print("Same vertex %d and %d",(v1,v2))
        if v1 in self.adjList:
            self.adjMatrix[self.adjList[v1]].append(v2)
        else:
            self.adjList[v1]=self.vCount
            self.adjMatrix[self.adjList[v1]].append(v2)
            self.vCount=self.vCount+1
        # self.adjMatrix[v1][v2]=1
        # self.adjMatrix[v2][v1]=1
    def removeEdge(self,v1,v2):
        if(v2 not in self.adjMatrix[v1]):
        # if(self.adjMatrix[v1][v2]==0):
            print("No Edge between %d and %d",(v1,v2))
            return
        self.adjMatrix[v1].remove(v2)
        # self.adjMatrix[v1][v2]=0
        # self.adjMatrix[v2][v1] = 0
    def containsEdge(self,v1,v2):
        return True if v2 in self.adjMatrix[v1] else False
    def len(self):
        return self.size

    def toString(self):
        for key,value in self.adjList.items():
            print("There is a path fron ",key," to  ",self.adjMatrix[value])
        print(self.adjMatrix)
        # for row in self.adjMatrix:
        #     for val in row:
        #         print('{:4}'.format(val),end=" "),
        #     print("\n")

def main():
    g = Graph(5)
    g.addEdge('andhra', 'bihar');
    g.addEdge('andhra', 'chennai');
    g.addEdge('bihar', 'chennai');
    g.addEdge('chennai', 'andhra');
    g.addEdge('chennai', 'delhi');

    g.removeEdge('chennai', 'andhra');




    # g.addEdge(0, 1);
    # g.addEdge(0, 2);
    # g.addEdge(1, 2);
    # g.addEdge(2, 0);
    # g.addEdge(2, 3);

    g.toString()

if __name__ == '__main__':
    main()

# def findCriticalConn(serversNum, connectionsNum, connections):
#     adjMatrix=[]
#     for i in range(serversNum):
#         adjMatrix.append([])
#         #0 for i in range(connectionsNum)
#     print(adjMatrix)
#     for i in range(len(connections)):
#         edge=list(connections[i])
#         adjMatrix[edge[0]].append(edge[1])
#     print(adjMatrix)
#
# findCriticalConn(6,5,((1,2),(1,3),(1,4),(3,4),(4,5)))

# class Graph:
#     def __init__(self,size):
#         self.adjMatrix=[]
#         for i in range(size):
#             self.adjMatrix.append([0 for i in range(size)])
#         self.size=size
#     def addEdge(self,v1,v2):
#         if(v1==v2):
#             print("Same vertex %d and %d",(v1,v2))
#         self.adjMatrix[v1][v2]=1
#         self.adjMatrix[v2][v1]=1
#     def removeEdge(self,v1,v2):
#         if(self.adjMatrix[v1][v2]==0):
#             print("No Edge between %d and %d",(v1,v2))
#             return
#         self.adjMatrix[v1][v2]=0
#         self.adjMatrix[v2][v1] = 0
#     def containsEdge(self,v1,v2):
#         return True if self.adjMatrix[v1][v2]>0 else False
#     def len(self):
#         return self.size
#
#     def toString(self):
#         for row in self.adjMatrix:
#             for val in row:
#                 print('{:4}'.format(val),end=" "),
#             print("\n")
#
# def main():
#     g = Graph(5)
#     g.addEdge(0, 1);
#     g.addEdge(0, 2);
#     g.addEdge(1, 2);
#     g.addEdge(2, 0);
#     g.addEdge(2, 3);
#
#     g.toString()
#
# if __name__ == '__main__':
#     main()