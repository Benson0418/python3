class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        def rec(s,res):
            ls=len(s)
            if ls==1:
                return (s,ls)
            A,lA=rec(s[:ls//2])
            B,lB=rec(s[ls//2:])
            if A[-1]==')' or B[0]=='(':
                return (A+B,len(A)+len(B))
            while 

            
