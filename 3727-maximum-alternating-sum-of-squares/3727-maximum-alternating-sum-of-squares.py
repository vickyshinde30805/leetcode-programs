class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)
        return sum(x * x for x in nums[len(nums)//2:]) - sum(x * x for x in nums[:len(nums)//2])