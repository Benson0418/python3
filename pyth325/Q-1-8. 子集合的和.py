n,P=map(int,input().split())
L=[int(x) for x in input().split()]
ans=0
def backtracking(num,idx,flag):
    global P,ans
    if num>P:
        return
    if flag and ans<num:
        ans=num
    if idx>=len(L)-1:
        return
    backtracking(num+L[idx+1],idx+1,True)
    backtracking(num,idx+1,False)
    
for i in range(len(L)):
    backtracking(L[i],i,True)

print(ans)
