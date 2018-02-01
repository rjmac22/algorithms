from PrimsJarnik.Edge import Edge;
from PrimsJarnik.Vertex import Vertex;
from PrimsJarnik.Algorithm import Algorithm;

node1 = Vertex("1");
node2 = Vertex("2");
node3 = Vertex("3");
node4 = Vertex("4");

edge1 = Edge(1, node1, node2);
edge2 = Edge(1, node1, node3);
edge3 = Edge(96, node1, node4);
edge4 = Edge(1, node3, node4);

node1.adjacenciesList.append(edge1);
node1.adjacenciesList.append(edge2);
node1.adjacenciesList.append(edge3);
node1.adjacenciesList.append(edge4);

unvistedList =[];
unvistedList.append(node1);
unvistedList.append(node2);
unvistedList.append(node3);
unvistedList.append(node4);


algorithm = Algorithm(unvistedList);
algorithm.constructSpanningTree(node1);
