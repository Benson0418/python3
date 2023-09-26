K,Q,R=map(int,input().split())
S=input()
L=[[int(x) for x in input().split()]for _ in range(Q)]
nL=[S]
for i in range(Q):
    s=['0']*K
    t=0
    for j in L[i]:
        s[j-1]=nL[i][t]
        t+=1
    n=''
    for k in s:
        n+=k
    nL.append(n)
for i in range(R):
    p=''
    for j in range(1,Q+1):
        p+=nL[j][i]
    print(*p,sep='')
