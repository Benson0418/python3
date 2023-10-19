class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def solve(s):
            S=[]
            for i in s:
                if i=='#':
                    if not S:
                        continue
                    S.pop()
                else:
                    S.append(i)
            return S
        return solve(s)==solve(t)
