n,M,S=map(int,input().split())
F=[int(x) for x in input().split()]
S-=M
S=abs(S)
curr=[0]*(S+1)
prev=[0]*(S+1)
for j in range(n):
    for i in range(1,S+1):
        if i>=F[j]:
            curr[i]=max(prev[i],F[j]+prev[i-F[j]])
        else:
            curr[i]=prev[i]
    curr,prev=prev,curr
print(sum(F)-prev[-1])
    


