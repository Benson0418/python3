from collections import deque
n=int(input())
M=[[]for _ in range(n)]
for i in range(1,n):
    x,w=map(int,input().split())
    M[i].append((x,w))
    M[x].append((i,w))

queue=deque([(0,0,0)])

max_t=0
max_c=0

visited=[False]*n
while queue:
    idx,t,c=queue.popleft()
    max_t=max(max_t,t)
    max_c=max(max_c,c)
    visited[idx]=True
    for x,w in M[idx]:
        if visited[x]:
            continue
        queue.append((x,t+1,c+w))

print(max_c)
print(max_t)
