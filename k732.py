n,m=map(int,input().split())
L=[[int(x) for x in input().split()]for _ in range(n)]
result=[]
for i in range(n):
    for j in range(m):
        count=0
        for s in range(i-L[i][j],i+L[i][j]+1):
            dis=L[i][j]-abs(s-i)
            for t in range(j-dis,j+dis+1):
                if 0<=s<n and 0<=t<m:
                    count+=L[s][t]
        if count%10==L[i][j]:
            result.append([i,j])
print(len(result))
for i in result:
    print(*i)
