class Solution1:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        時間複雜度O(nlogn)
        空間複雜度為O(n)
        sub列表並非真正的遞增子序列
        """
        sub = []
        for num in nums:
            idx = bisect_left(sub,num)
            if idx == len(sub):
                sub.append(num)
            else:
                sub[idx] = num
        return len(sub)

class Solution2:
    def lengthOfLIS(self, nums: List[int]) -> int:
      """
      時間複雜度為O(n^2)
      空間複雜度為O(n)
      """
        n = len(nums)
        dp = n*[1]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return max(dp)
