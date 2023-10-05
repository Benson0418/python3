class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robbing(nums[0:len(nums)-1]),self.robbing(nums[1:len(nums)]))

    def robbing(self, t: List[int]) -> int:
      rob1=rob2=0
      for i in t:
        rob1,rob2=rob2,max(rob1+i,rob2)
      return rob2
