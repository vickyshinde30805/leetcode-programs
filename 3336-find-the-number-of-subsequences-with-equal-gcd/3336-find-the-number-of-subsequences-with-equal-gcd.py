from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        # dp[(gcd1, gcd2)] = number of ways
        dp = {(0, 0): 1}

        for num in nums:
            new_dp = dp.copy()

            for (g1, g2), count in dp.items():

                # Put num in subsequence 1
                ng1 = gcd(g1, num)
                new_dp[(ng1, g2)] = (
                    new_dp.get((ng1, g2), 0) + count
                ) % MOD

                # Put num in subsequence 2
                ng2 = gcd(g2, num)
                new_dp[(g1, ng2)] = (
                    new_dp.get((g1, ng2), 0) + count
                ) % MOD

            dp = new_dp

        ans = 0

        for (g1, g2), count in dp.items():
            if g1 == g2 and g1 != 0:
                ans = (ans + count) % MOD

        return ans
        