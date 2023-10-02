n=int(input())
L=sorted([int(x) for x in input().split()])
T=sorted([int(x) for x in input().split()])
count=0
a=0
b=0
while a<n and b<n:
    if L[a]<T[b]:
        count+=1
        a+=1
        b+=1
    else:
        b+=1
print(count)
