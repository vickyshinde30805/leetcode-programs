from typing import List

class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        odds = [x for x in nums1 if x & 1]
        evens = [x for x in nums1 if x % 2 == 0]

        # Already uniform
        if not odds or not evens:
            return True

        # Smallest odd cannot change parity.
        min_odd = min(odds)

        # Every even must have a smaller odd.
        return all(min_odd < e for e in evens)