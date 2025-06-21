from heapq import heappush,heappop
n,m=map(int,input().split())
adj=[[]for _ in range(n)]
for _ in range(m):
    a,b,c=map(int,input().split())
    adj[a].append((b,c))
    adj[b].append((a,c))
dis=[float('inf')]*n
locked=[False]*n
dis[0]=0
pq=[(0,0)]

while pq:
    dv,v=heappop(pq)
    if locked[v]:continue
    locked[v]=True
    for i,j in adj[v]:
        if dv+j<dis[i]:
            dis[i]=dv+j
            heappush(pq,(dis[i],i))
max_dis=float('-inf')
res=0
for i in dis:
    if i==float('inf'):
        res+=1
    else:
        max_dis=max(max_dis,i)
print(max_dis)
print(res)
