A=input()
B=input()
m,n=len(A),len(B)

prev=[0]*n
curr=[0]*n
for i in range(m):
    curr[0]=1 if A[i]==B[0] else prev[0]
    for j in range(1,n):
        curr[j]=prev[j-1]+1 if A[i]==B[j] else max(prev[j],curr[j-1])
    prev,curr=curr,prev
print(prev[-1])
        

