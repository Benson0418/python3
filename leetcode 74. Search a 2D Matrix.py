class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        R,C=len(matrix),len(matrix[0])
        left=0
        right=R-1
        L=[]
        while left<=right:
            mid=left+(right-left)//2
            if matrix[mid][0]<=target<=matrix[mid][-1]:
                L=matrix[mid]
                break
            elif target<matrix[mid][0]:
                right=mid-1
            else:
                left=mid+1
        if not L:
            return False
        left=0
        right=C-1
        while left<=right:
            mid=left+(right-left)//2
            if L[mid]==target:
                return True
            elif target<L[mid]:
                right=mid-1
            else:
                left=mid+1
        return False
