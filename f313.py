R,C,k,m=map(int,input().split())
L=[[int(x) for x in input().split()]for _ in range(R)]
for x in range(m):
    tempL=[]
    for y in L:
        tempL.append(y.copy())
    for i in range(R):
        for j in range(C):
            if L[i][j]==-1:
                continue
            minus=L[i][j]//k
            if i-1>=0 and L[i-1][j]>=0:
                tempL[i][j]-=minus
                tempL[i][j]+=L[i-1][j]//k
            if i+1<R and L[i+1][j]>=0:
                tempL[i][j]-=minus
                tempL[i][j]+=L[i+1][j]//k
            if j-1>=0 and L[i][j-1]>=0:
                tempL[i][j]-=minus
                tempL[i][j]+=L[i][j-1]//k
            if j+1<C and L[i][j+1]>=0:
                tempL[i][j]-=minus
                tempL[i][j]+=L[i][j+1]//k
    L,tempL=tempL,[]
outmax=-1
outmin=2147483647
for i in range(R):
    for j in range(C):
        if L[i][j]>outmax:
            outmax=L[i][j]
        if L[i][j]<outmin and L[i][j]!=-1:
            outmin=L[i][j]
print(outmin)
print(outmax)

