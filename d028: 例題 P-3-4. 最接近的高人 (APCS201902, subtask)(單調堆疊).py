n=int(input())
L=[0]+[int(x) for x in input().split()]
res=0
stack=[(0,float('inf'))]
for i,j in enumerate(L):
    if i==0:
        continue
    while j>=stack[-1][1]:
        stack.pop()
    res+=i-stack[-1][0]
    stack.append((i,j))
print(res)
        
