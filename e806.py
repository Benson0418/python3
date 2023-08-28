N=int(input())
L=[int(x) for x in input().split()]
E=int(input())
G=[int(x) for x in input().split()]
Lc=[]
Ls=[]
Gc=[]
Gs=[]
flag=True
for i in range(0,N*2,2):
    Lc.append(L[i])
    Ls.append(L[i+1])
for i in range(0,E*2,2):
    Gc.append(G[i])
    Gs.append(G[i+1])
L=Lc+Gc
G=Ls+Gs
T=[0]*1001
for i in zip(L,G):
    T[i[0]]=T[i[0]]+i[1]
for i in range(1000,-1,-1):
    if T[i]!=0:
        print(f"{i}:{T[i]}")
        flag=False
if flag:
    print("NULL!")
