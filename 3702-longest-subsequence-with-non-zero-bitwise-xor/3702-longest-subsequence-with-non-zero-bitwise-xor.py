class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        all_zero = True

        for x in nums:
            xor ^= x
            if x != 0:
                all_zero = False

        if xor != 0:
            return len(nums)
        if all_zero:
            return 0
        return len(nums) - 1