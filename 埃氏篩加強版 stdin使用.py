L=[1,0]*1000001
L[2]=0
L[1]=1
for i in range(3,1000001,2):
    if L[i]==0:
        for j in range(i*i,1000001,i+i):
            L[j]=1
from sys import stdin
for s in stdin:
    o=int(s)
    if o==0:
        break
    print(L[o])
