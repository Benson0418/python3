n,k=map(int,input().split())
N=[int(x) for x in input().split()]
K=[int(x) for x in input().split()]

for i in K:
    flag=True
    L,R=0,n-1
    while L<=R:
        mid=(L+R)//2
        if i == N[mid]:
            print(mid+1)
            flag=False
            break
        elif i>N[mid]:
            L=mid+1
        else:
            R=mid-1
    if flag:
        print(0)
