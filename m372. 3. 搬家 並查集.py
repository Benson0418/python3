directions=[(-1,0),(0,-1)] # 上左
dL={
    'X':[(1,0),(-1,0),(0,1),(0,-1)],# 下上右左
    'I':[(1,0),(-1,0)],
    'H':[(0,1),(0,-1)],
    'L':[(-1,0),(0,1)],
    '7':[(1,0),(0,-1)],
    'F':[(1,0),(0,1)],
    'J':[(-1,0),(0,-1)]
    }
n,m=map(int,input().split())
grid=[input() for _ in range(n)]
parent=[i for i in range(0,n*m)]

def find(p1):
    if parent[p1]!=p1:
        parent[p1]=find(parent[p1])
    return parent[p1]

def union(n1,n2):
    p1,p2=find(n1),find(n2)
    parent[p1]=parent[p2]
    return

for i in range(n):
    for j in range(m):
        if grid[i][j]!='0':
            for x,y in directions:
                nx=x+i
                ny=y+j
                if 0<=nx<n and 0<=ny<m and grid[nx][ny]!='0' and (x,y) in dL[grid[i][j]] and (-x,-y) in dL[grid[nx][ny]]:
                    union(i*m+j,nx*m+ny)
counter=dict()
for i in range(n):
    for j in range(m):
        if grid[i][j] != '0':
            p=find(i*m+j)
            counter[p]=counter.get(p,0)+1
print(max(counter.values()))
