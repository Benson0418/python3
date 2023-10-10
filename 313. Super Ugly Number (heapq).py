# 第一種解法
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglys=[1]
        pcount=[0]*len(primes)
        while len(uglys) != n:
            ugly=min(primes[i]*uglys[pcount[i]] for i in range(len(primes)))
            uglys.append(ugly)
            for i in range(len(primes)):
                if primes[i]*uglys[pcount[i]] == ugly:
                    pcount[i] += 1
        return uglys[n-1]

# 第二種解法
from heapq import heapify, heappop, heappush

class Solution2:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        nums = primes.copy()
        heapify(nums)
        res = 1
        for i in range(n - 1):
            res = heappop(nums)
            for prime in primes:
                heappush(nums, res * prime)
                if res % prime == 0:
                    break
        return res
