#方法一:使用遞迴寫法(容易超時或是記憶體過大)
class Solution:
    def maxCoins(self, nums: List[int]) -> int: 
        nums=[1]+nums+[1]
        @lru_cache(maxsize=None)
        def sol(start,end):
            if end-start<=1:
                return 0
            elif end-start<=2:
                return nums[start]*nums[start+1]*nums[end]
            else:
                res=0
                for i in range(start+1,end):
                    res=max(res,sol(start,i)+sol(i,end)+nums[start]*nums[i]*nums[end])
                return res
        return sol(0,len(nums)-1)

#方法二:將遞迴思想轉為動態規劃
