directions=[(-1,0),(0,-1)]
directions_2=[(1,0),(0,1),(-1,0),(0,-1)]
m,n,k=map(int,input().split())
grid=[[0]*(n+2)]
for _ in range(m):
    grid.append([0]+[int(x) for x in input().split()]+[0])
grid.append([0]*(n+2))
parent=list(range(m*n))

size=0
count=0
curr_size=0
curr_count=0
size_arr=[1]*(m*n)

for i in range(1,m+1):
    for j in range(1,n+1):
        if grid[i][j]==1:
            curr_count+=1

def find(A):
    if A!=parent[A]:
        parent[A]=find(parent[A])
    return parent[A]

def union(A,B):
    global curr_count,curr_size
    pA,pB=find(A),find(B)
    if pA!=pB:
        if pA<pB:
            size_arr[pA]+=size_arr[pB]
            parent[pB]=parent[pA]
            curr_size=max(curr_size,size_arr[pA])
        else:
            size_arr[pB]+=size_arr[pA]
            parent[pA]=parent[pB]
            curr_size=max(curr_size,size_arr[pB])
        curr_count-=1
        
for i in range(1,m+1):
    for j in range(1,n+1):
        if grid[i][j]==0:
            continue
        for x,y in directions:
            nx,ny=x+i,y+j
            if grid[nx][ny]==1:
                union(nx*n+ny-n-1,i*n+j-n-1)
            
size+=curr_size
count+=curr_count

op=[int(x) for x in input().split()]
for idx in range(k):
    cx,cy=op[2*idx],op[2*idx+1]
    if grid[cx][cy]==1:
        size+=curr_size
        count+=curr_count
        continue
    grid[cx][cy]=1
    curr_count+=1
    for x,y in directions_2:
        nx,ny=cx+x,cy+y
        if grid[nx][ny]==1:
            union(nx*n+ny-n-1,cx*n+cy-n-1)
    size+=curr_size
    count+=curr_count
print(size)
print(count)
    
    

            
            
