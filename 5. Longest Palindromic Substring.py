class Solution:
    def longestPalindrome(self, s: str) -> str:
        def find(l,r):
            nonlocal res,n
            while l-1>=0 and r+1<n:
                if s[l-1]==s[r+1]:
                    l=l-1
                    r=r+1
                else:
                    break
            if len(res)<r-l+1:
                res=s[l:r+1]
            return
        n=len(s)
        res=""
        for i in range(n):
            l=r=i
            find(l,r)
            if i+1<n and s[i]==s[i+1]:
                l=i
                r=i+1
                find(l,r)
        return res
