R,C,N=map(int,input().split())
k=1
L=[[0 for _ in range(R)] for _ in range(C)]
Ltemp=[[0 for _ in range(R)] for _ in range(C)]
for j in range(R):
    for i in range(C):
        L[j][i] = k
        k += 1

if N == 1:
    for i in range(R):
        print(*L[i])
else:
    for n in range(2,N+1):
        if n%2==0:
            for j in range(C):
                for i in range(R):
                    Ltemp[j][(i-1)%R]=L[j][i%R]
        else:
            for i in range(R):
                for j in range(C):
                    Ltemp[(i-1)%R][j]=L[i%R][j]
        L = [row[:] for row in Ltemp]
        Ltemp = [[0 for _ in range(R)] for _ in range(C)]

    for i in range(R):
        print(*L[i])
