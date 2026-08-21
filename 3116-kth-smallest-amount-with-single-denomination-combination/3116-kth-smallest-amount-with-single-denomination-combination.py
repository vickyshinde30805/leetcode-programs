from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Remove redundant coins (e.g. 6 if 3 exists)
        coins.sort()
        arr = []
        for c in coins:
            if all(c % x for x in arr):
                arr.append(c)
        coins = arr
        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        # Precompute (lcm, sign) for every subset
        subsets = []

        def dfs(idx, cur_lcm, bits):
            for i in range(idx, n):
                nlcm = lcm(cur_lcm, coins[i])
                subsets.append((nlcm, 1 if bits % 2 == 0 else -1))
                dfs(i + 1, nlcm, bits + 1)

        dfs(0, 1, 0)

        def count(x):
            res = 0
            for l, s in subsets:
                if l <= x:
                    res += s * (x // l)
            return res

        lo, hi = 1, min(coins) * k

        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1

        return lo