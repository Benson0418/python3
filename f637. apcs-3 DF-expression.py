def dfs(n,x,y):
    global idx,res
    if idx>=lenL:
        return
    idx+=1
    if L[idx]=='1':
        for i in range(x,x+n):
            for j in range(y,y+n):
                res+=1
    elif L[idx]=='2':
        nn=n//2
        dfs(nn,x,y)
        dfs(nn,x,y+nn)
        dfs(nn,x+nn,y)
        dfs(nn,x+nn,y+nn)
    return
L=input()
lenL=len(L)
n=int(input())
idx=-1
res=0
dfs(n,0,0)
print(res)


# 以下為更進一步的精簡
def dfs(n):
    global idx,res
    if idx>=lenL:
        return
    idx+=1
    if L[idx]=='1':
        res+=n*n
    elif L[idx]=='2':
        for _ in range(4):
            dfs(n//2)
    return
L=input()
lenL=len(L)
n=int(input())
idx=-1
res=0
dfs(n)

print(res)
