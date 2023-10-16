class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res=[[1]]
        path=[1]
        for i in range(rowIndex):
            for j in range(1,len(res[-1])):
                path.append(res[-1][j]+res[-1][j-1])
            path.append(1)
            res.append(path)
            path=[1]
        return res[-1]
        
