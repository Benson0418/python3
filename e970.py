N=int(input())
r=[int(x) for x in input().split()]
B=r[-1]
s=0
for i in range(1,N+1):
    if i%B==1:
        s+=r[i-1]
if s%N==0:
    print(N,end=" ")
else:
    print(s%N,end=" ")
print(r[s%N-1])
    
