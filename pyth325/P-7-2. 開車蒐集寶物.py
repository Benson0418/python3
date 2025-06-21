#解1
n,m=map(int,input().split())
V=[int(x) for x in input().split()]

parent=list(range(n))

def find(A):
    if A!=parent[A]:
        parent[A]=find(parent[A])
    return parent[A]

def union(A,B):
    pA,pB=find(A),find(B)
    if parent[pA]!=parent[pB]:
        parent[pB]=parent[pA]
        V[pA]+=V[pB]
    
for _ in range(m):
    union(*map(int,input().split()))

print(max(V))


#解2
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
