class Solution:
    def partitionString(self, s: str) -> int:
        r=0
        t=set()
        res=0
        while r<len(s):
            if s[r] not in t:
                t.add(s[r])
            else:
                res+=1
                t.clear()
                t.add(s[r])
            r+=1
        return res+1
