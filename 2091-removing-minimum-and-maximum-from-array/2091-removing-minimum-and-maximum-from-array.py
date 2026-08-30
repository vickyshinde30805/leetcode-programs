class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        if min_idx > max_idx:
            min_idx, max_idx = max_idx, min_idx

        # Case 1: Remove both from the front
        front = max_idx + 1

        # Case 2: Remove both from the back
        back = n - min_idx

        # Case 3: Remove one from the front and one from the back
        both = (min_idx + 1) + (n - max_idx)

        return min(front, back, both)