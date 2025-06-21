N=int(input())
for _ in range(N):
    t=int(input())
    L=[]
    for i in range(9,1,-1):
        while t%i==0:
            t//=i
            L.append(i)
    if t!=1:
        print(-1)
    elif len(L)==0:
        print(1)
    else:
        L.reverse()
        print(*L,sep="")
        
