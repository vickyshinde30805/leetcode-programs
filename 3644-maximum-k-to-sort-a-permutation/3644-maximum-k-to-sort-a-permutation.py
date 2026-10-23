class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k = -1

        for i in range(len(nums)):
            if nums[i] != i:
                k &= nums[i]

        return max(k, 0)