N,P=input().split()
N=int(N)
list_=[]
result=[]
nresult=-1
n=0
for i in P:
    list_.append(int(i))
list_=list_[::-1]
for i in range(0,len(P),N):
    result.append(sum(list_[i:i+N]))
for i in range(len(result)):
    if result[i]>=nresult:
        nresult=result[i]
        n=i+1
print(n,nresult,sep=" ")
    
