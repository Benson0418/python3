n=int(input())
W=[int(x) for x in input().split()]
F=[int(x) for x in input().split()]
T=sorted([(W[i]/F[i],i) for i in range(n)])

w=0
res=0
for _,i in T:
    res+=w*F[i]
    w+=W[i]
print(res)
    
