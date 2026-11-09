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

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = set()
path=[]
lim=2

if dls(graph, 'A', 'E', visited, path,lim):
    print("Path",path)
