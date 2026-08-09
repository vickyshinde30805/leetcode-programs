from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix sum
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        @lru_cache(None)
        def dp(i, M):
            if i >= n:
                return 0

            # if can take all
            if i + 2*M >= n:
                return suffix[i]

            res = 0
            for X in range(1, 2*M + 1):
                res = max(res, suffix[i] - dp(i + X, max(M, X)))

            return res

        return dp(0, 1)