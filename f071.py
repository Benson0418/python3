a,b,c=map(int,input().split())
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]
m=0
flag=True
for i in range(len(A)):
    if a==A[i]:
        m+=B[i]
    if b==A[i]:
        m+=B[i]
    if c==A[i]:
        flag=False
        m-=B[i]
if flag:
    m*=2
if m<=0:
    print(0)
else:
    print(m)
