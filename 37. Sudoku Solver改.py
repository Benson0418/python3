class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """
        hashmap=[]
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    hashmap.append((i,j))
        n=len(hashmap)

        def valid_sudoku(a,b):
            for i in range(9):
                if board[i][b]==board[a][b] and i!=a:
                    return False
                if board[a][i]==board[a][b] and i!=b:
                    return False
            t=a//3*3
            u=b//3*3
            for i in range(t,t+3):
                for j in range(u,u+3):
                     if board[i][j]==board[a][b] and i!=a and j!=b:
                        return False
            return True

        def backtracking(idx):
            if idx == n:
                return True
            a, b = hashmap[idx]
            for i in range(1, 10):
                board[a][b]=str(i)
                if not valid_sudoku(a,b):
                    board[a][b] = '.'
                    continue
                if  backtracking(idx + 1):
                    return True
                board[a][b] = '.'
 
        backtracking(0)
        return

solver = Solution()
test_1 = [
    ["8",".",".",".",".",".",".",".","."],
    [".",".","3","6",".",".",".",".","."],
    [".","7",".",".","9",".","2",".","."],
    [".","5",".",".",".","7",".",".","."],
    [".",".",".",".","4","5","7",".","."],
    [".",".",".","1",".",".",".","3","."],
    [".",".","1",".",".",".",".","6","8"],
    [".",".","8","5",".",".",".","1","."],
    [".","9",".",".",".",".","4",".","."]
]
test_2 = [
    [".",".","5","3",".",".",".",".","."],
    ["8",".",".",".",".",".",".","2","."],
    [".","7",".",".","1",".","5",".","."],
    ["4",".",".",".","5","3",".",".","."],
    [".","1",".",".","7",".",".",".","6"],
    [".",".","3","2",".",".",".","8","."],
    [".","6",".","5",".",".",".",".","9"],
    [".",".","4",".",".",".",".","3","."],
    [".",".",".",".",".","9","7",".","."]
]

solver.solveSudoku(test_1)
solver.solveSudoku(test_2)

print(*test_1,sep='\n')
print()
print(*test_2,sep='\n')
