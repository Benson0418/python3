while True:
    try:
        N=int(input())
    except:
        break
    L=[[0,0]]
    for _ in range(N):
        L.append([int(x) for x in input().split()])
    S=[[0]*101 for _ in range(N+1)]
    for i in range(1,N+1):
        for j in range(1,101):
            if L[i][0]>j:
                S[i][j]=S[i-1][j]
            else:
                S[i][j]=max(L[i][1]+S[i-1][j-L[i][0]],S[i-1][j])
    print(S[N][100])
    
