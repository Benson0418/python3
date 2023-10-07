n=int(input())
L=[0]+[int(x) for x in input().split()]
if n==1:
    print(L[1])
elif n==2:
    print(L[2])
else:
    a,b=L[1],max(L[1],L[2])
    for i in range(3,n+1):
        a,b=b,max(b,a+L[i])
    print(b)
