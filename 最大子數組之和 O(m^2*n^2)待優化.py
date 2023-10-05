m,n=map(int,input().split())
L=[[int(x) for x in input().split()] for _ in range(m)]
for i in range(m):
    for j in range(1,n):
        L[i][j]+=L[i][j-1]
for i in range(1,m):
    for j in range(n):
        L[i][j]+=L[i-1][j]
result=0
for i in range(m):
    for j in range(n):
        for k in range(i+1):
            result=max(result,L[i][j]-L[k][j],L[i][j])
        for l in range(j+1):
            result=max(result,L[i][j]-L[i][l],L[i][j])
print(result)
