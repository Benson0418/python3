N=int(input())
L=[1]+[int(x) for x in input().split()]
S=0
for i in range(1,N+1):
    a=L[i]-L[i-1]
    if a>0:
       S+=a*3
    else:
        S+=a*(-2)
print(S)
