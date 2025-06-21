n,W=map(int,input().split())
L=[0]+[int(x) for x in input().split()]
V=[0]+[int(x) for x in input().split()]

curr=[0]*(W+1)
prev=[0]*(W+1)
for i in range(1,n+1):
    for j in range(1,W+1):
        if j>=L[i]:
            curr[j]=max(prev[j-L[i]]+V[i],prev[j])
        else:
            curr[j]=prev[j]
    curr,prev=prev,curr
print(prev[-1])
