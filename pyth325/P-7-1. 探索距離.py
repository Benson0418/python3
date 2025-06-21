from collections import deque

n,m=map(int,input().split())
s=int(input())
L=[[]for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    L[a].append(b)
queue=deque([(s,0)])
res=0
total_dis=0
visited=[False]*n
while queue:
    v,d=queue.popleft()
    if visited[v]:
        continue
    total_dis+=d
    res+=1
    visited[v]=True
    d+=1
    for k in L[v]:
        if visited[k]:
            continue
        queue.append((k,d))
print(res-1)
print(total_dis)
