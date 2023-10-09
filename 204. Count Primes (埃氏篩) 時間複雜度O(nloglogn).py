class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        p = [1]*n
        for j in range(4, n, 2):
            p[j] = 0
        for i in range(3, int(n**0.5)+1, 2):
            if p[i]:
                for j in range(i*i, n, i+i): 
                    p[j] = 0

        return sum(p[2:])


class Solution2:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0
        l = [1] * n
        l[0] = l[1] = 0

        m = 2

        while m * m < n:
            if l[m] == 1:
                l[m * m: n: m] = [0] * (1 + (n - m * m - 1) // m)
            m += 1 if m ==2 else 2
        return sum(l)
