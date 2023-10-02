n=int(input())
L=sorted([int(x) for x in input().split()])
for i in range(1,n):
    L[i]+=L[i-1]
print(sum(L))
