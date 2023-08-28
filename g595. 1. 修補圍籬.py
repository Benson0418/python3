n=int(input())
a=[int(x) for x in input().split()]
total=0
for i in range(n):
     if a[i]==0:
        if i==0:
            total+=a[1]
        elif i==n-1:
            total+=a[n-2]
        else:
            total+=min(a[i-1],a[i+1])
print(total)
