directions=[(1,0),(-1,0),(0,1),(0,-1)]
visited=[[False]*15 for _ in range(15)]
num_list=[]
while True:
    R,C=map(int,input().split())
    if R==0 and C==0:
        break
    grid=[input() for _ in range(R)]
    res=0
    
    
    def max_res(num_list):
        global res
        lres=len(str(res))
        if lres>len(num_list):
            return
        res=max(res,int("".join(num_list)))
        return
    
    def backtracking(x,y):
        global res
        visited[x][y]=True
        num_list.append(grid[x][y])

        move=False
        for s,t in directions:
            nx,ny=x+s,y+t
            if 0<=nx<R and 0<=ny<C and grid[nx][ny]!='#' and not visited[nx][ny]:
                move=True
                backtracking(nx,ny)

        if not move:
            max_res(num_list)
        num_list.pop()
            
        visited[x][y]=False
        return
        
    for i in range(R):
        for j in range(C):
            if grid[i][j]!='#':
                backtracking(i,j)
    print(res)
