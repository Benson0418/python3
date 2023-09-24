class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      R=len(grid)
      C=len(grid[0])
      direction=[(1,0),(-1,0),(0,1),(0,-1)]
      time=-1
      queue=[]
      for i in range(R):
        for j in range(C):
          if grid[i][j]==2:
            queue.append([i,j])
      while queue:
        for _ in range(len(queue)):
          x,y=queue.pop(0)
          for a,b in direction:
            tempx=x+a
            tempy=y+b
            if 0<=tempx<R and 0<=tempy<C and grid[tempx][tempy]==1:
              grid[tempx][tempy]=2
              queue.append([tempx,tempy])
        time+=1
      for i in range(R):
        for j in range(C):
          if grid[i][j]==1:
            return -1
      return max(0,time)
    

        
      
        
