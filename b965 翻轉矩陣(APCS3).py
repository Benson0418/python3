while True:
    try:
        R,C,M=map(int,input().split())
    except EOFError:
        break
    L=[]
    for i in range(R):
        L.append([int(x) for x in input().split()])
    op=[int(x) for x in input().split()][::-1]
    for opi in op:
        if opi==0:
            Ltemp=[[0 for _ in range(len(L))] for _ in range(len(L[0]))]
            for i in range(len(L)):
                for j in range(len(L[0])):
                    Ltemp[len(L[0])-1-j][i]=L[i][j]
            L=Ltemp
        else:
            L=L[::-1]
    print(len(L),len(L[0]))
    for i in L:
        print(*i)
