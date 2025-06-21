from heapq import heappop,heappush
n,m=map(int,input().split())
linked=[False]*n
res=0

M=[[]for _ in range(n)]
for _ in range(m):
    u,v,w=map(int,input().split())
    M[u].append((v,w))
    M[v].append((u,w))

pq=[]

for s,t in M[0]:
    heappush(pq,(t,s))
linked[0]=True

while pq:
    a,b=heappop(pq)
    if linked[b]:continue
    res+=a
    linked[b]=True
    for s,t in M[b]:
        heappush(pq,(t,s))

print(res if all(linked) else -1)
