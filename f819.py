N=int(input())
L=[]
Y=[]
S=0
for i in range(N):
    L.append([int(x) for x in input().split()])
for i in L:
    if i[1]>100:
        S+=(i[1]-100)*5
        Y.append(i[0])
print(*sorted(Y))
print(S)
