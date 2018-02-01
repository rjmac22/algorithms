
from Dijkstra.Vertex import Vertex;
from Dijkstra.Edge import Edge;
from Dijkstra.Algorithm import Algorithm;



nodeA = Vertex("A");
nodeB = Vertex("B");
nodeC = Vertex("C");
nodeD = Vertex("D");
nodeE = Vertex("E");
nodeF = Vertex("F");
nodeG = Vertex("G");
nodeH = Vertex("H");

edge1 = Edge(5, nodeA, nodeB);
edge2 = Edge(9, nodeA, nodeE);
edge3 = Edge(8, nodeA, nodeH);
edge4 = Edge(15, nodeB, nodeD);
edge5 = Edge(12, nodeB, nodeC);
edge6 = Edge(4, nodeB, nodeH);
edge7 = Edge(7, nodeH, nodeC);
edge8 = Edge(6, nodeH, nodeF);
edge9 = Edge(5, nodeE, nodeH);
edge10 = Edge(4, nodeE, nodeF);
edge11 = Edge(20, nodeE, nodeG);
edge12 = Edge(9, nodeD, nodeG);
edge13 = Edge(3, nodeC, nodeD);
edge14 = Edge(11, nodeC, nodeG);
edge15 = Edge(1, nodeF, nodeC);
edge16 = Edge(13, nodeF, nodeG);


nodeA.adjacenciesList.append(edge1);
nodeA.adjacenciesList.append(edge2);
nodeA.adjacenciesList.append(edge3);

nodeB.adjacenciesList.append(edge4);
nodeB.adjacenciesList.append(edge5);
nodeB.adjacenciesList.append(edge6);

nodeC.adjacenciesList.append(edge13);
nodeC.adjacenciesList.append(edge14);

nodeD.adjacenciesList.append(edge12);

nodeE.adjacenciesList.append(edge9);
nodeE.adjacenciesList.append(edge10);
nodeE.adjacenciesList.append(edge11);

nodeF.adjacenciesList.append(edge15);
nodeF.adjacenciesList.append(edge16);

nodeH.adjacenciesList.append(edge7);
nodeH.adjacenciesList.append(edge6);



vertexList = {nodeA, nodeB, nodeC, nodeD,nodeE, nodeF, nodeG, nodeH };

algorithm = Algorithm();
algorithm.calculateShortestPath(vertexList, nodeA);
algorithm.getSortestPathTo(nodeD);
algorithm.getSortestPathTo(nodeH);