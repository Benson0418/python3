n,W=map(int,input().split())
L=[0]+list(zip(map(int,input().split()),map(int,input().split())))
grid_prv=[0]*(W+1)
grid_crr=[0]*(W+1)
for a,b in enumerate(L):
    for i in range(1,W+1):
        if a==0:
            break
        if b[0]>i:
            grid_crr[i]=grid_prv[i]
        else:
            grid_crr[i]=max(grid_prv[i],grid_prv[i-b[0]]+b[1])
    grid_prv,grid_crr=grid_crr,grid_prv
print(grid_prv[-1])
