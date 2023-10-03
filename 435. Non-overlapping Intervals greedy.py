class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        k=0
        end=intervals[0][1]
        for i in intervals[1:]:
            if i[0]<end:
                k+=1
                end=min(end,i[1])
            else:
                end=i[1]
        return k
