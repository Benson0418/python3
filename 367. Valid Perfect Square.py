class Solution:
    def isPerfectSquare(self, num: int) -> bool:
      if num==1:
        return 1
      l,r=1,num
      while l<=r:
        mid=l+(r-l)//2
        mid2=mid*mid
        if mid2==num:
          return True
        elif mid2<num:
          l=mid+1
        else:
          r=mid-1
      return False
