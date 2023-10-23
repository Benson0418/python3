from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        R,C=len(grid),len(grid[0])
        visited=[[False]*C for _ in range(R)]
        queue=deque()
        res=0
        def bfs(i,j):
            nonlocal visited,queue
            temp=1
            visited[i][j]=True
            queue.append((i,j))
            while queue:
                x,y=queue.popleft()
                for a,b in directions:
                    nx,ny=x+a,y+b
                    if not 0<=nx<R or not 0<=ny<C or grid[nx][ny]==0 or visited[nx][ny]:
                        continue
                    temp+=1
                    queue.append((nx,ny))
                    visited[nx][ny]=True
            return temp
        
        for i in range(R):
            for j in range(C):
                if grid[i][j]==0 or visited[i][j]:
                    continue
                res=max(res,bfs(i,j))
        return res
                
