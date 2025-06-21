from collections import deque

n=int(input())
parent=[-1]+[0]*n
h=[0]*(n+1)
deg=[0]*(n+1)
queue=deque()

for i in range(1,n+1):
    T=[int(x) for x in input().split()]
    if T[0]==0:
        queue.append(i)
    else:
        deg[i]=len(T)-1
        for j in T[1:]:
            parent[j]=i

root=parent.index(0)
print(root)
while queue:
    t=queue.pop()
    if parent[t]==0:break
    h[parent[t]]=max(h[t]+1,h[parent[t]])
    deg[parent[t]]-=1
    if deg[parent[t]]<=0:
        queue.append(parent[t])

print(sum(h))
