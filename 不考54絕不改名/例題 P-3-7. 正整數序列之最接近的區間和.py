n,K=map(int,input().split())
A=[int(x) for x in input().split()]
res=0
temp=0
left=0
count=0
for right in range(n):
    temp+=A[right]
    if temp<=K:
        if res==temp:
            count+=1
        elif res<temp:
            count=1
            res=temp
        continue
    else:
        while temp>K:
            temp-=A[left]
            left+=1
        if res==temp:
            count+=1
        elif res<temp:
            count=1
            res=temp
print(res)
print(count)
    
    
