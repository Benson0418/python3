
# 解1:
from bisect import bisect_left

n=int(input())
L=[int(x) for x in input().split()]

def sol(L):
    if len(L)<=1:
        return 0
    mid=len(L)//2
    res=0
    lL,rL=L[:mid],L[mid:]
    res+=sol(lL)+sol(rL)
    rL.sort()
    for k in lL:
        res+=bisect_left(rL,k)
    return res
print(sol(L))

#解2:
n=int(input())
L=[int(x) for x in input().split()]

def sol(L):
    if len(L)<=1:
        return 0
    mid=len(L)//2
    res=0
    lL,rL=L[:mid],L[mid:]
    res+=sol(lL)+sol(rL)
    lL.sort()
    rL.sort()
    k=0
    for i in lL:
        while k<len(rL) and i>rL[k]:
            k+=1
        res+=k
    return res

print(sol(L))
