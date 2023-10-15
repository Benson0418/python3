class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c==0 or c==1:
            return True
        l,r=1,int(c**0.5)
        if r*r==c:
            return True
        while l<=r:
            if l*l+r*r==c:
                return True
            if l*l+r*r>c:
                r-=1
            else:
                l+=1
        return False
