def dfs(graph, node, goal, visited, path):
    if node==goal:
        path.append(node)
        return True
    visited.add(node)
    path.append(node)

    for c in graph[node]:
        if c not in visited:
            if dfs(graph,c,goal,visited, path):
                return True
    path.pop()

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
if dfs(graph, 'A', 'E', visited, path):
    print("Path",path)
