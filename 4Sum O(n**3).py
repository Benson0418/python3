class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
      L=set()
      nums.sort()
      n=len(nums)
      for i in range(n-3):
        for j in range(i+1,n-2):
          a,b=j+1,n-1
          while a<b:
            t=nums[i]+nums[j]+nums[a]+nums[b]
            if t==target:
              L.add((nums[i],nums[j],nums[a],nums[b]))
              a+=1
              b-=1
            elif t<target:
              a+=1
            else:
              b-=1
      return list(L)
