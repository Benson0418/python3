# 試著推出f(n)=p*f(n-1)+p(n-2)的解(模1e9+7)，時間複雜度O(klogn)，k為詢問次數

mod=1000000007
from math import log2,floor
import time

def matrix_mul(a,b):
    return [[(a[0][0]*b[0][0]+a[0][1]*b[1][0])%mod,
             (a[0][0]*b[0][1]+a[0][1]*b[1][1])%mod],
        [(a[1][0]*b[0][0]+a[1][1]*b[1][0])%mod,
         (a[1][0]*b[0][1]+a[1][1]*b[1][1])%mod]]

def matrix_fast_exp(n):
    for _ in range(n):
        base_matrix.append(matrix_mul(base_matrix[-1],base_matrix[-1]))

t1=time.time()
p,q,r=map(int,input().split())
a0,a1=map(int,input().split())
a2=p*a0+q*a1+r
T=int(input())
L=[int(x) for x in input().split()]
maxL=max(L)

base_matrix=[[[0,1],[p,q]]]
matrix_fast_exp(floor(log2(maxL)))

for i in L:
    if i==0:
        print(a0)
        continue
    elif i==1:
        print(a1)
        continue
    res=[[a0,a1],[a1,a2]]
    c=0
    while i>0:
        if i&1:
            res=matrix_mul(base_matrix[c],res)
        i>>=1
        c+=1
    print(res[0][0])
t2=time.time()

print(t2-t1)
        
    
