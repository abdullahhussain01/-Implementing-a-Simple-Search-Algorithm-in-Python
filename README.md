# -Implementing-a-Simple-Search-Algorithm-in-Python
          1.	Research the Depth-First Search (DFS) & Breadth First Search (BFS)Algorithms:
Depth-First Search (DFS) and Breadth-First Search (BFS) are two of the most basic and commonly used algorithms for searching through a graph or tree. Both algorithms are used to traverse a graph or tree and find a particular node or path. 
DFS: DFS starts at the root node and explores as far as possible along each branch before backtracking. It uses a stack to keep track of the nodes to visit next. DFS is good for finding a path between two nodes if one exists, and it can also be used to find all the nodes in a connected component of a graph.
 BFS: BFS starts at the root node and explores all the nodes at the current depth before moving on to the next depth. It uses a queue to keep track of the nodes to visit next. BFS is good for finding the shortest path between two nodes, and it can also be used to find all the nodes in a connected component of a graph.
          2.	Apply DFS and BFS on Romanian example:
The Romanian example is a classic problem in graph theory, which involves finding the shortest path between two cities in Romania using different search algorithms.
we want to find the shortest path between the cities Arad and Bucharest, we can apply Depth-First Search (DFS) and Breadth-First Search (BFS) algorithms on the graph.
Depth-First Search (DFS):
Depth-First Search (DFS):
Depth-First Search (DFS) is an algorithm that explores a graph by visiting a node and recursively visiting all its unvisited neighbors before backtracking. To find the path from Arad to Bucharest using DFS, we can start at Arad and recursively visit its neighbors until we reach Bucharest. 
we can find one possible path from Arad to Bucharest as follows:
1.	Start at Arad and mark it as visited
2.	Visit Timisoara and mark it as visited
3.	Visit Lugoj and mark it as visited
4.	Visit Mehadia and mark it as visited
5.	Visit Dobreta and mark it as visited
6.	Backtrack to Mehadia
7.	Visit Craiova and mark it as visited
8.	Visit Rimnicu Vilcea and mark it as visited
9.	Visit Sibiu and mark it as visited
10.	Visit Fagaras and mark it as visited
11.	Visit Bucharest and mark it as visited.
12.       Construct the path: [Arad, Timisoara, Lugoj, Mehadia, Dobreta, Craiova, Rimnicu Vilcea, Sibiu, Fagaras, Bucharest]
Breadth-First Search (BFS):
BFS is an algorithm that explores a graph by visiting all the neighboring nodes of a given node before visiting any of their children.
we can find the path from Arad to Bucharest as follows:
1.	Start at node Arad and add it to the queue.
2.	Visit node Arad, and mark it as visited.
3.	Add the neighbors of Arad (Zerind, Sibiu, Timisoara) to the queue.
4.	Visit node Sibiu, mark it as visited, and add its unvisited neighbors (Oradea, Fagaras, Rimnicu Vilcea) to the queue.
5.	Visit node Fagaras, mark it as visited, and add its unvisited neighbor (Bucharest) to the queue.
6.	Visit node Bucharest, mark it as visited, and terminate the search.
7.	Construct the path: [Arad, Sibiu, Fagaras, Bucharest].
So the shortest path from Arad to Bucharest using BFS is ['Arad', 'Sibiu', 'Fagaras', 'Bucharest'].
