def dls(graph, node, goal, visited, path,lim):
    if node==goal:
        path.append(node)
        return True
    
    if lim<=0:
        return False
    
    visited.add(node)
    path.append(node)

    for c in graph[node]:
        if c not in visited:
            if dls(graph,c,goal,visited, path,lim-1):
                return True
            
    path.pop()
    visited.remove(node)
    return False

def iddfs(graph, node, goal):
    depth = 0
    while True:
        visited = set()
        path = []
        if dls(graph, node, goal, visited, path, depth):
            return path
        depth += 1

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

res = iddfs(graph, 'A', 'E')
print("Path",res)