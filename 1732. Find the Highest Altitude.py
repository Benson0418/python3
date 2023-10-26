class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n=len(gain)
        crr=res=0
        for i in range(n):
            crr+=gain[i]
            res=max(res,crr)
        return res
