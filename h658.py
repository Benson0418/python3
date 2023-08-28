X,Y=map(int,input().split())
N=int(input())
L=[]
for i in range(N):
    L.append([int(x) for x in input().split()])
Min=2147483647
A,B=0,0
for i in L:
    if Min>abs(X-i[0])**2+abs(Y-i[1])**2:
        Min=abs(X-i[0])**2+abs(Y-i[1])**2
        A,B=i[0],i[1]
print(A,B)
