n=int(input())
P=[int(x) for x in input().split()]
res=0

left=0
for right in range(n):
    if P[right]<P[left]:
        left=right
        continue
    res=max(res,P[right]-P[left])
print(res)
