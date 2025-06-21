N=int(input())
X=[int(x) for x in input().split()]
Y=[int(x) for x in input().split()]
XY=sorted(list(zip(X,Y)),key=lambda x:(x[0],-x[1]))
nXY=[]
mono=[]
k=0
for i in range(N):
    if XY[i][0]>k:
        nXY.append(XY[i][1])
        k=XY[i][0]
for i in range(len(nXY)):
    while mono and nXY[i]>mono[-1]:
        mono.pop()
    mono.append(nXY[i])
print(len(mono))
