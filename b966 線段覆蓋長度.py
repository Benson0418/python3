N=int(input())
L=[]
c=0
for _ in range(N):
    L.append([int(x) for x in input().split()])
L.sort()
left,right=0,0
for i in L:
    if i[0]>right:
        c+=right-left
        left=i[0]
        right=i[1]
    else:
        right=max(right,i[1])
c+=right-left
print(c)
