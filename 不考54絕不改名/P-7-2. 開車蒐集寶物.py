from collections import deque
n,m=map(int,input().split())
V=[int(x) for x in input().split()]
M=[[]for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    M[a].append(b)
    M[b].append(a)
res=0
visited=[False]*n
queue=deque()

def bfs(x):
    global queue
    if visited[x]:
        return 0
    temp_res=0
    queue.append(x)
    while queue:
        t=queue.popleft()
        if visited[t]:
            continue
        visited[t]=True
        temp_res+=V[t]
        for i in M[t]:
            if not visited[i]:
                queue.append(i)
    return temp_res
            
   
for i in range(n):
    res=max(bfs(i),res)
print(res)
