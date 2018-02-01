from collections import deque


# Sample graph implemented as a dictionary
graph = {'A': ['B', 'C', 'E'],
         'B': ['A', 'D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B', 'D'],
         'F': ['C'],
         'G': ['C']
         }



#Visits all the nodes of a graph(connected component) using BFS

def bfs_shortest_path(graph, start, goal):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to b checked
#     queue = [[start]]
    queue = deque([start])
    # return path if start is goal
    if start == goal:
        return "That was easy! Start = goal"
    
    
    # keep looping until all nodes are checked
    while queue:
        # pop shallowest node(first node) from queue
        path = queue.popleft()
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            
            # go though all neighbour nodes , construct a new path
            # and push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighour is goal
                if neighbour == goal:
                    return new_path
                
            # add node to list of checked nodes
            explored.append(node)
            
    # in case there's no path between the 2 nodes
    return "So sorry, but a connecting path doesn't exist"
    
    return explored 
        
print(bfs_shortest_path(graph, 'G', 'D'))