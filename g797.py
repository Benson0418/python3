N,M=map(int,input().split())
X=[int(x) for x in input().split()]
Y=[]
for i in range(M):
    temp=[]
    X,Y=X[:N//2],X[N//2:]
    for j in range(N//2):
        temp.append(X[j])
        temp.append(Y[j])
    X=temp
print(*X)
    
