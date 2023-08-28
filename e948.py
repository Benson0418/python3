N=int(input())
L=[]
for i in range(N):
    L.append([int(x) for x in input().split()])
for i in L:
    if i[0]==1:
        a=i[3]*13.7+i[2]*5.0-i[1]*6.8+66
    else:
        a=i[3]*9.6+i[2]*1.8-i[1]*4.7+655
    print(f"{a:.2f}")
