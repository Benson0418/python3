res=[]
n,m=map(int,input().split())
for i in range(n,m+1):
    k=str(i)
    l=len(k)
    r=0
    for j in k:
        r+=int(j)**l
    if r==i:
        res.append(k)
print(' '.join(res) if res else 'none')
