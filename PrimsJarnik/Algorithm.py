import heapq;

class Algorithm(object):
    
    def __init__(self, unvistedList):
        self.unvisitedList = unvistedList;
        self.spanningTree = [];
        self.edgeHeap = [];
        self.fullCost = 0;
        
        
    def constructSpanningTree(self, vertex):
        
        self.unvisitedList.remove(vertex);
        
        while self.unvisitedList:
            
            for edge in vertex.adjacenciesList:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap, edge);
                    
            minEdge = heapq.heappop(self.edgeHeap);
            
            self.spanningTree.append(minEdge);
            print("Edge added to spanning tree: %s - %s" % (minEdge.startVertex.name, minEdge.targetVertex.name));
            self.fullCost += minEdge.weight;
            
            vertex = minEdge.targetVertex;
            self.unvisitedList.remove(vertex);
            
    def getSpanningTree(self):
        return self.spanningTree;
            