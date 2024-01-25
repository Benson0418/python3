from collections import Counter
n,m=map(int,input().split())

res=0
L=[]
for _ in range(m):
    u,v,w=map(int,input().split())
    L.append((w,u,v))
L.sort()

parent=list(range(n))
def find(A):
    if parent[A]!=A:
        parent[A]=find(parent[A])
    return parent[A]

def union(w,A,B):
    global res
    pA,pB=find(A),find(B)
    if pA==pB:
        return
    if pA<pB:
       parent[pB]=parent[pA]
    else:
       parent[pA]=parent[pB]
    res+=w

for i in range(m):
    w,u,v=L[i]
    union(w,u,v)

for i in range(n):
    find(i)

C=Counter(parent)
print(res if len(C)==1 else -1)


