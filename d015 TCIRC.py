m,n,K=map(int,input().split())
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
result=0
di={}
for a in A:
    di[a]=di.get(a,0)+1
for b in B:
    result+=di.get(K-b,0)
print(result)
