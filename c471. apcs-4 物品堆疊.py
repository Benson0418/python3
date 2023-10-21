N=int(input())
W=list(map(int,input().split()))
F=list(map(int,input().split()))
A=[]
res=0
temp=0
for i in range(N):
    if F[i]!=0:
        A.append([i,W[i]/F[i]])
A.sort(key=lambda x:x[1])
for a,_ in A:
    res+=temp*F[a]
    temp+=W[a]
print(res)
