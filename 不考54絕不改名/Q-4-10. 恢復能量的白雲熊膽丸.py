n,m=map(int,input().split())
P=[int(x) for x in input().split()]

left,right=max(P),sum(P)
def greedy(F,count):
    energy=F
    for i in range(n):      
        if energy<P[i]:
            energy=F
            if count<=0:
                return False
            count-=1
        energy-=P[i]
    return True

while left<right:
    mid=(left+right)//2
    if greedy(mid,m):
        right=mid
    else:
        left=mid+1
print(greedy(7,m))

print(right)

        
            
            
    
