class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n=len(s)
        res=0
        p=0
        z=o=0
        while p<n:
            if s[p]=='0':
                if o==0:
                    z+=1
                else:
                    res=max(res,o*2)
                    z,o=1,0
            else:
                if o<z:
                    o+=1
                else:
                    res=max(res,o*2)
                    z=o=0
            p+=1
        res=max(res,o*2)
        return res
