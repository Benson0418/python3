from collections import Counter

n,k=map(int,input().split())
L=[int(x) for x in input().split()]
M=Counter()

for i in range(k):
    M[L[i]]+=1

res=len(M)
temp=res
for right in range(k,n):
    left=right-k
    if L[right] not in M:
        temp+=1
    M[L[right]]+=1
    M[L[left]]-=1
    if M[L[left]]<=0:
        M.pop(L[left])
        temp-=1
    res=max(res,temp)

print(res)
    
