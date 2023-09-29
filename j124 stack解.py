L=[int(x) for x in input().split()]
stack=[[L[0],0]]
result=0
for i in L:
    if i>0:
        result+=abs(stack[-1][0]-i)
        stack.append([i,2+i%2])
    else:
        stack[-1][1]-=1
        while stack[-1][1]==0:
            stack.pop()
            stack[-1][1]-=1
print(result)
            
        
        
