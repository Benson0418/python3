N=int(input())
L=sorted([tuple(int(x) for x in input().split()) for _ in range(N)])

curr=0
res=0
for i in range(N):
    if L[i][0]<=curr:
        if L[i][1]>curr:
            res+=L[i][1]-curr
            curr=L[i][1]
    else:
        res+=L[i][1]-L[i][0]
        curr=L[i][1]
print(res)
