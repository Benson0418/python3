N=int(input())
H=[int(x) for x in input().split()]
W=[int(x) for x in input().split()]
m=2147483647
p=[0]*2
for i in range(N):
    if H[i]*W[i]<m:
        m=H[i]*W[i]
        p[0]=H[i]
        p[1]=W[i]
print(*p)
