class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,columns=len(board),len(board[0])
        visited=set()
        def DFS(r,c,i):
            if i==len(word):
                return True
            if r<0 or c<0 or r>=rows or c>=columns or (r,c) in visited or word[i]!=board[r][c]:
                return False
            visited.add((r,c))
            res=DFS(r+1,c,i+1) or DFS(r-1,c,i+1) or DFS(r,c-1,i+1) or DFS(r,c+1,i+1)
            visited.discard((r,c))
            return res

        for i in range(rows):
            for j in range(columns):
                if DFS(i,j,0):return True
                    
        return False
