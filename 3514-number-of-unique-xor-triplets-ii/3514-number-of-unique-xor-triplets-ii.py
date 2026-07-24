from typing import List

class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        mx = max(nums) << 1

        # All possible XORs of two elements
        pair = [False] * mx
        for a in nums:
            for b in nums:
                pair[a ^ b] = True

        # All possible XORs of three elements
        ans = [False] * mx
        for x in range(mx):
            if pair[x]:
                for c in nums:
                    ans[x ^ c] = True

        return sum(ans)