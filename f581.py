n,m=map(int,input().split())
p=[int(x) for x in input().split()]
q=[int(x) for x in input().split()]
for i in range(1,n):
    p[i]+=p[i-1]
move=0
for i in q:
    if move>0:
        x=i+p[move-1]
    else:
        x=i
    if x>p[-1]:
        move=0
        x%=p[-1]
    left,right=move,n-1
    while left<right:
        mid=left+(right-left)//2
        if p[mid]>=x:
            right=mid
        else:
            left=mid+1
    move=(right+1)%n
print(move)
