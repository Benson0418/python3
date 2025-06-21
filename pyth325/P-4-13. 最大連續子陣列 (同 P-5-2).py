n=int(input())
A=[int(x) for x in input().split()]

res=0
temp=0
for i in range(n):
    temp+=A[i]
    if temp<0:
        temp=0
        continue
    res=max(res,temp)
print(res)
