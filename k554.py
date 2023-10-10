N,M=map(int,input().split())
L=[[int(x) for x in input().split()]for _ in range(N)]
G=[[0]*M for _ in range(N)]
di=[(1,0),(0,1),(-1,0),(0,-1),(0,0)]
for i in range(N):
    for j in range(M):
        if L[i][j]==1:
            for a,b in di:
                if 0<=i+a<N and 0<=j+b<M:
                    G[i+a][j+b]+=1
        elif L[i][j]==2:
            for k in range(N):
                G[k][j]+=1
            for l in range(M):
                G[i][l]+=1
            G[i][j]-=1
for i in G:
    print(*i)
