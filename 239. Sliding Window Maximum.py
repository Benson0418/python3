class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        queue=deque()
        res=[]
        for i in range(k):
            if not queue or queue[-1][0]>nums[i]:
                queue.append((nums[i],i))
            else:
                while queue and queue[-1][0]<=nums[i]:
                    queue.pop()
                queue.append((nums[i],i))
        res.append(queue[0][0])
        l=0
        r=k
        while r<n:
            if not queue or queue[-1][0]>nums[r]:
                queue.append((nums[r],r))
            else:
                while queue and queue[-1][0]<=nums[r]:
                    queue.pop()
                queue.append((nums[r],r))
            r+=1
            l+=1
            if queue[0][1]<l:
                queue.popleft()
            res.append(queue[0][0])
        return res
