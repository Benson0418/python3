m,n=map(int,input().split())
M=[[int(x) for x in input().split()] for _ in range(m)]
directions=[(1,0),(-1,0),(0,1),(0,-1)]
x,y=0,0
start=M[0][0]
for i in range(m):
    for j in range(n):
        if M[i][j]<start:
            start=M[i][j]
            x,y=i,j
res=0
while True:
    res+=M[x][y]
    M[x][y]=float('inf')
    temp=float('inf')
    new_x,new_y=0,0
    for s,t in directions:
        nx=s+x
        ny=t+y
        if 0<=nx<m and 0<=ny<n and M[nx][ny]<temp:
            temp=M[nx][ny]
            new_x,new_y=nx,ny
    if temp==float('inf'):
        break
    x,y=new_x,new_y
print(res)
        
    
    
