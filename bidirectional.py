from collections import deque


def bidirectional_search(graph, start, goal):

    if start == goal:
        return [start]

    reverse_graph = {node: [] for node in graph}

    for node in graph:
        for n in graph[node]:
            reverse_graph[n].append(node)

    frontier_fwd = deque([start])
    frontier_bwd = deque([goal])

    visited_fwd = {start}
    visited_bwd = {goal}

    parent_fwd = {start: None}
    parent_bwd = {goal: None}

    while frontier_fwd and frontier_bwd:

        node_fwd = frontier_fwd.popleft()
        for n in graph[node_fwd]:
            if n not in visited_fwd:
                visited_fwd.add(n)
                parent_fwd[n] = node_fwd
                frontier_fwd.append(n)

            if n in visited_bwd:
                return build_path(n, parent_fwd, parent_bwd)

        node_bwd = frontier_bwd.popleft()
        for n in reverse_graph[node_bwd]:
            if n not in visited_bwd:
                visited_bwd.add(n)
                parent_bwd[n] = node_bwd
                frontier_bwd.append(n)

            if n in visited_fwd:
                return build_path(n, parent_fwd, parent_bwd)

    return None


def build_path(meet, parent_fwd, parent_bwd):

    path = []
    node = meet

    while node is not None:
        path.append(node)
        node = parent_fwd[node]

    path.reverse()

    node = meet

    while parent_bwd[node] is not None:
        node = parent_bwd[node]
        path.append(node)

    return path


graph = {
    1: [3],
    3: [5],
    5: [2],
    2: []
}

result = bidirectional_search(graph, 1, 2)

if result:
    print("Path:", result)
else:
    print("Path not found")