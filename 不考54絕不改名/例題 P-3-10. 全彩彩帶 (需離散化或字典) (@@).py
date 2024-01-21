from collections import Counter
n=int(input())
L=[int(x) for x in input().split()]
S=len(set(L))
M=Counter()

l=r=0
while len(M)<S:
    M[L[r]]+=1
    r+=1
while M[L[l]]>1:
    M[L[l]]-=1
    l+=1
    
res=r-l
temp=res
left=l

for right in range(r,n):
    M[L[right]]+=1
    while M[L[left]]>1:
        M[L[left]]-=1
        left+=1
    temp=right-left+1
    res=min(res,temp)
print(res)
    
