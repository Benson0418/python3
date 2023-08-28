N=int(input())
l=[int(x) for x in input().split()]
L=[]
for i in range(N,0,-1):
    if i not in l:
        L.append(i)
for i in L:
    print(f"No. {i}")
