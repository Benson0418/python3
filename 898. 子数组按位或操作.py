class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()
        pre = set()
        for num in arr:
            cur = {num}
            for pre_num in pre:
                cur.add(num | pre_num)
            res |= cur
            pre = cur
        return len(res)
