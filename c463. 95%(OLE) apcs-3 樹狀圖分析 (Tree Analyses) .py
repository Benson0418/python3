n=int(input())
tree=dict()
root={i for i in range(1,n+1)}
for i in range(1,n+1):
    x,*l=map(int,input().split())
    if x==0:
        tree[i]=None
    else:
        l=set(l)
        for j in l:
            root.discard(j)
        tree[i]=l
root=root.pop()
print(root)
depth_sum=0
def dfs(node):
    global depth_sum
    if not tree[node]:
        return 0
    t=0
    for i in tree[node]:
        t=max(t,dfs(i)+1)
    depth_sum+=t
    return t
dfs(root)
print(depth_sum)

