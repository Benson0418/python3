m,n,K=map(int,input().split())
A=set(map(int,input().split()))
B=[int(x) for x in input().split()]
count=0
for i in B:
    if K-i in A:
        count+=1
print(count)
