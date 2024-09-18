from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums=list(map(str,nums))
        def cmp(n1,n2):
            return -1 if n1+n2>n2+n1 else 1
        nums.sort(key=cmp_to_key(cmp))
        return str(int(''.join(nums)))
