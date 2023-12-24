mod=1000000007

from math import log2,floor

def matrix_mul(a,b):
    p=len(a)
    q=len(b[0])
    r=len(b)
    res_matrix=[[0]*q for _ in range (p)]
    for i in range(p):
        for j in range(q):
            for k in range(r):
                res_matrix[i][j]+=a[i][k]*b[k][j]
    for i in range(p):
        for j in range(q):
            res_matrix[i][j]%=mod
    return res_matrix

def matrix_fast_exp(n):
    for _ in range(n):
        base_matrix.append(matrix_mul(base_matrix[-1],base_matrix[-1]))

p,q,r=map(int,input().split())
a0,a1=map(int,input().split())
T=int(input())
L=[int(x) for x in input().split()]
maxL=max(L)

base_matrix=[[[0,1,0],[q,p,1],[0,0,1]]]
matrix_fast_exp(floor(log2(maxL-1)))

for i in L:
    if i==0:
        print(a0)
        continue
    if i==1:
        print(a1)
        continue
    i-=1
    res=[[a0],[a1],[r]]
    c=0
    while i>0:
        if i&1:
            res=matrix_mul(base_matrix[c],res)
        i>>=1
        c+=1
    print(res[1][0])
    
