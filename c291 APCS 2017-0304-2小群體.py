N=int(input())
total=0
list_=[int(x) for x in input().split()]
flag=[False]*N
for i in range(N):
    if flag[i]:continue
    flag[i]=True
    total+=1
    if list_[i]==i:continue
    q = list_[i]
    while list_[q]!=i:
        flag[q]=True
        q=list_[q]
    flag[q]=True
print(total)
        
