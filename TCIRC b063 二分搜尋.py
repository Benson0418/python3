n=int(input())
L=sorted([int(x) for x in input().split()])
Q=int(input())
T=[[int(x) for x in input().split()] for _ in range(Q)]
for i in T:
    left=0
    right=len(L)-1
    while left<right:
        mid=left+(right-left)//2
        if L[mid]>=i[0]:
            right=mid
        else:
            left=mid+1
    X=right if L[right]>=i[0] else -1
    if X==-1:
        print(0)
        continue
    left=0
    right=len(L)-1
    while left<right:
        mid=left+(right-left+1)//2
        if L[mid]<=i[1]:
            left=mid
        else:
            right=mid-1
    Y=left if L[left]<=i[1] else -1
    if Y==-1:
        print(0)
        continue
    print(Y-X+1)
    
