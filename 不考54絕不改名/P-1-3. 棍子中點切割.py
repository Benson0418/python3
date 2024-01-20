from bisect import bisect_right

N,L=map(int,input().split())
K=[int(x) for x in input().split()]
cost=0
def sol(start,end,K):
    global cost
    if len(K)==0 or end<=start+1:
        return
    mid=(start+end)/2
    t=bisect_right(K,mid)
    cost+=end-start
    if t==len(K):
        sol(start,K[-1],K[:len(K)-1])
    elif t==0:
        sol(K[0],end,K[1:])
    else:
        p=t-1 if mid-K[t-1]<=K[t]-mid else t
        sol(start,K[p],K[:p])
        sol(K[p],end,K[p+1:])
    return
sol(0,L,K)
print(cost) 
