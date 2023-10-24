from collections import deque
directions=[(1,0),(-1,0),(0,1),(0,-1)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        safe=[]
        queue=deque()
        for i in range(n):
            if board[0][i]=="O":
                safe.append((0,i))
                queue.append((0,i))
            if board[m-1][i]=="O":
                safe.append((m-1,i))
                queue.append((m-1,i))
        for i in range(1,m-1):
            if board[i][0]=="O":
                safe.append((i,0))
                queue.append((i,0))
            if board[i][n-1]=="O":
                safe.append((i,n-1))
                queue.append((i,n-1))
        while queue:
            x,y=queue.popleft()
            for a,b in directions:
                nx,ny=x+a,y+b
                if not 0<=nx<m or not 0<=ny<n or board[nx][ny]=="X" or (nx,ny) in safe:
                    continue
                queue.append((nx,ny))
                safe.append((nx,ny))
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i,j) not in safe:
                    board[i][j]="X"
                
