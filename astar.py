import heapq

def h(n, goal):
    vertical = abs(n[0] - goal[0])*2
    horizontal = abs(n[1] - goal[1])

    return horizontal + vertical


def astar(maze, start, goal):

    rows=len(maze)
    cols=len(maze[0])

    frontier = []
    heapq.heappush(frontier, (h(start, goal), start))

    visited=set()
    parent={start: None}
    gCost={start: 0}

    directions=[(0,1), (1,0), (-1,0), (0,-1)]

    while frontier:

        f, node = heapq.heappop(frontier)

        if node in visited:
            continue

        if node == goal:
            return build_path(parent, goal), gCost[goal]

        visited.add(node)

        r,c=node

        for dr,dc in directions:

            nr=r+dr
            nc=c+dc

            child=(nr,nc)

            if(0<=nr<rows and 0<=nc<cols
                and maze[nr][nc]!=1):

                if dr==0:
                    moveCost=1
                else:
                    moveCost=2

                newCost=gCost[node]+moveCost

                if child not in gCost or newCost < gCost[child]:

                    gCost[child] = newCost
                    parent[child] = node

                    fCost = newCost + h(child, goal)

                    heapq.heappush(frontier, (fCost, child))

                    if child in visited:
                        visited.remove(child)

    return None, None


def build_path(parent, goal):

    path=[]
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    return path[::-1]


maze = [
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]
]

start=(0,0)
goal=(4,4)

path,cost = astar(maze, start, goal)

if path:
    print("Path:", path)
    print("Path Cost:", cost)
else:
    print("No path found")
