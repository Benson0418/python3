class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def find(node):
            if parent[node]!=node:
                parent[node]=find(parent[node])
            return parent[node]

        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            parent[p1]=p2
            return
        
        directions=[(-1,0),(0,-1)]
        R,C=len(grid),len(grid[0])

        parent=[-1]*(1+R*C)
        for i in range(R):
            for j in range(C):
                if grid[i][j]=='1':
                    parent[i*C+j]=i*C+j
                    for x,y in directions:
                        nx,ny=x+i,y+j
                        if 0<=nx and 0<=ny and grid[nx][ny]=='1':
                            union(parent[nx*C+ny],parent[i*C+j])
        res=set()
        for i in range(R):
            for j in range(C):
                if grid[i][j]=='1':
                    res.add(find(parent[i*C+j]))

        return len(res)
        
