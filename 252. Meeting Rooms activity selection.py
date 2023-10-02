"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        n=len(intervals)
        for i in range(1,n):
            if intervals[i].start<intervals[i-1].end:
                return False
        return True
