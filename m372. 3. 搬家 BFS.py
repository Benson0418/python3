from collections import deque
def bfs(a,b):
    global visited,queue,temp
    visited[a][b]=True
    temp+=1
    queue.append((a,b))
    while queue:
        x,y=queue.popleft()
        for s,t in d[L[x][y]]:
            nx,ny=x+s,y+t
            if not 0<=nx<n or not 0<=ny<m or L[nx][ny]=='0' or visited[nx][ny]:
                continue
            elif (-s,-t) not in d[L[nx][ny]]:
                continue
            else:
                queue.append((nx,ny))
                visited[nx][ny]=True
                temp+=1
                
d={
    'X':[(1,0),(-1,0),(0,1),(0,-1)],
    'I':[(1,0),(-1,0)],
    'H':[(0,-1),(0,1)],
    'L':[(0,1),(-1,0)],
    '7':[(1,0),(0,-1)],
    'F':[(1,0),(0,1)],
    'J':[(0,-1),(-1,0)]
    }
n,m=map(int,input().split())
L=[]
for _ in range(n):
    L.append(input())
visited=[[False]*m for _ in range(n)]
queue=deque()
res=0
temp=0
for i in range(n):
    for j in range(m):
        if L[i][j]=='0' or visited[i][j]:
            continue
        temp=0
        bfs(i,j)
        res=max(res,temp)
print(res)
        
