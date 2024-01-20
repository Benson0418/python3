#sol1

P=10009
n=int(input())
L=[int(x) for x in input().split()]
count=0
def backtracking(num,idx,flag):
    global count
    if num%P==1 and flag:
        count+=1
    if idx>=len(L)-1:
        return
    backtracking(num*L[idx+1],idx+1,True)
    backtracking(num,idx+1,False)
for i in range(len(L)):
    backtracking(L[i],i,True)
print(count)




# sol2
P=10009
n=int(input())
L=[int(x) for x in input().split()]
count=0
def backtracking(L):
    global count
    if len(L)==1:
        if L[0]%P==1:
            count+=1
        return L
    mid=len(L)//2
    pL,qL=backtracking(L[:mid]),backtracking(L[mid:])
    res=pL+qL
    for i in pL:
        for j in qL:
            T=i*j
            if T%P==1:
                count+=1
            res.append(i*j)
    return res
backtracking(L)
print(count)
