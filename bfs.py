import heapq

def h(n):
    vertical=abs(n[0]-goal[0])*2
    horizontal=abs(n[1]-goal[1])
    return horizontal+vertical

def greedy(maze, start, goal):
    rows=len(maze)
    cols=len(maze[0])
    frontier = []
    heapq.heappush(frontier, (h(start),start))
    vis=set()
    parent={start:None}
    dir=[(0,1),(1,0),(-1,0),(0,-1)]
    while frontier:
        _,n=heapq.heappop(frontier)
        if n in vis:
            continue
        if n==goal:
            return build_path(parent,goal)
        vis.add(n)
        r,c=n
        for dr,dc in dir:
            nr,nc=r+dr, c+dc
            child=(nr,nc)
            if(0<=nr<rows and 0<=nc<cols and maze[nr][nc]!=1 and child not in vis):
                if child not in parent:
                    parent[child]=n
                    heapq.heappush(frontier,(h(child),child))
    return None

def build_path(parent,goal):
    path=[]
    node=goal
    while node is not None:
        path.append(node)
        node=parent[node]
    return path[::-1]

def calcCost(path):
    cost=0
    for i in range(1,len(path)):
        r1,c1=path[i-1]
        r2,c2=path[i]
        if r1==r2:
            cost+=1
        else:
            cost+=2
    return cost
    
maze=[
    [0,0,0,1,0],
    [1,1,0,1,0],
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0]]
start=(0,0)
goal=(4,4)
res=greedy(maze,start,goal)
print(res)
print(calcCost(res))
               