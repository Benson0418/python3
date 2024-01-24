from collections import deque
n,p,l,r=map(int,input().split())
S=[int(x) for x in input().split()]
visited=[False]*n
queue=deque([(0,0)])
flag=-1
while queue:
    t,u=queue.popleft()
    if S[t]==p:
        flag=u
        break
    if visited[t]:
        continue
    while 0<=t<n and t!=S[t]:
        visited[t]=True
        t=S[t]
    if t<0 or t>=n or visited[t]:
        continue
    visited[t]=True
    a,b=t-l,t+r
    if 0<=a<n:
        queue.append((a,u+1))
    if 0<=b<n:
        queue.append((b,u+1))
print(flag)
