from math import ceil

n,k=map(int,input().split())
L=sorted(list(set(map(int,input().split()))))
left,right=1, ceil((L[-1]-L[0])/k)

def greedy(R):
    idx=0
    global k
    for time in range(k):
        next=L[idx]+R
        while idx<len(L) and L[idx]<=next:
            idx+=1
        if idx>=len(L):
            return True
    return idx>=len(L)

while left<right:
    mid=(right+left)//2
    if greedy(mid):
        right=mid
    else:
        left=mid+1
        
print(right)
    
    


