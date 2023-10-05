n=int(input())
for _ in range(n):
    L=[int(x) for x in input().split()]
    t=len(L)
    l=r=0
    result=float('-inf')
    e=0
    while r<len(L):
        if e>=0:
            r+=1
        else:
            l=r=r+1
            e=0
        if r<len(L):
            e+=L[r]
            result=max(result,e)
    print(result)
