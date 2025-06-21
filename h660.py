X,R,V=map(int,input().split())
N=int(input())
L=[]
for i in range(N):
    L.append([int(x) for x in input().split()])
for i in L:
    if i[0]<X-R or i[0]>X+R:
        continue
    elif i[1]<=V:
        X=i[0]
    elif i[0]>=X:
        X-=15
    else:
        X+=15
print(X)
