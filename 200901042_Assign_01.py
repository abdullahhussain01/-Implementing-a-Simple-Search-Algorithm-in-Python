graph = {
    'Arad': {'Zerind': 75,'Sibiu': 140, 'Timisoara': 118, },
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Sibiu': {'Arad': 140, 'Fagaras': 99, 'Oradea': 151, 'Rimnicu Vilcea': 80},
    'Oradea': {'Sibiu': 151, 'Zerind': 71},
    'Fagaras': {'Bucharest': 211, 'Sibiu': 99},
    'Rimnicu Vilcea': {'Craiova': 146, 'Pitesti': 97, 'Sibiu': 80},
    'Lugoj': {'Mehadia': 70, 'Timisoara': 111},
    'Mehadia':{'Lugoj':70 , 'Dobreta':75},
    'Dobreta': {'Craiova': 120, 'Mehadia': 75},
    'Craiova': {'Dobreta': 120, 'Pitesti': 138, 'Rimnicu Vilcea': 146},
    'Pitesti': {'Bucharest': 101, 'Craiova': 138, 'Rimnicu Vilcea': 97},
    'Bucharest': {'Fagaras': 211, 'Giurgiu': 90, 'Pitesti': 101, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Hirsova': 98, 'Vaslui': 142},
    'Hirsova': {'Eforie': 86, 'Urziceni': 98},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Iasi': 92, 'Urziceni': 142},
    'Iasi': {'Neamt': 87, 'Vaslui': 92},
    'Neamt': {'Iasi': 87}
}
# DFS implementation:
def dfs(graph, start, goal):
    stack = [(start, [start])] # stack to store the path to the current node
    visited = set() # to keep track of visited nodes

    while stack:
        (vertex, path) = stack.pop()

        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)

            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))

def bfs(graph, start, goal):
    queue = [(start, [start])]
    visited = set()

    while queue:
        (vertex, path) = queue.pop(0)

        if vertex not in visited:
            if vertex == goal:
                return path
            visited.add(vertex)

            for neighbor in graph[vertex]:
                queue.append((neighbor, path + [neighbor]))

# Testing the algorithms
start = 'Arad'
goal = 'Bucharest'

print("Shortest path using DFS:", dfs(graph, start, goal))
print("Shortest path using BFS:", bfs(graph, start, goal))
