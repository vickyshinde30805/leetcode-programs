
from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        BASE = 911382323
        MOD1 = 10**9 + 7
        MOD2 = 10**9 + 9

        def check(length):
            power1 = pow(BASE, length, MOD1)
            power2 = pow(BASE, length, MOD2)

            h1 = h2 = 0

            # Calculate hash of first window
            for i in range(length):
                h1 = (h1 * BASE + nums[i]) % MOD1
                h2 = (h2 * BASE + nums[i]) % MOD2

            freq = {(h1, h2): 1}

            # Sliding window with rolling hash
            for i in range(length, n):
                old = nums[i - length]
                new = nums[i]

                h1 = (h1 * BASE - old * power1 + new) % MOD1
                h2 = (h2 * BASE - old * power2 + new) % MOD2

                key = (h1, h2)
                freq[key] = freq.get(key, 0) + 1

            return any(count == 1 for count in freq.values())

        # Binary search for minimum valid length
        left, right = 1, n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
