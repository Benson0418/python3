class Solution:
  def isValidSudoku(self, board: List[List[str]]) -> bool:
    for i in board:
      hashmap=set()
      for j in i:
        if j!='.':
          if j in hashmap:
            return False
          hashmap.add(j)
    for i in zip(*board):
      hashmap=set()
      for j in i:
        if j!='.':
          if j in hashmap:
            return False
          hashmap.add(j)
    for i in range(0,8,3):
      for j in range(0,8,3):
        hashmap=set()
        for k in range(i,i+3):
          for l in range(j,j+3):
            if board[k][l]!='.':
              if board[k][l] in hashmap:
                return False
              hashmap.add(board[k][l])
    return True
