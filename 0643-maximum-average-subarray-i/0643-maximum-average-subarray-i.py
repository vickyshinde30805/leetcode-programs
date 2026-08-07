class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        addition=0
        for i in range(k):
            addition+=nums[i]
        maxsum=addition

        for i in range(k,len(nums)):
            addition+=nums[i]
            addition-=nums[i-k]

            maxsum=max(maxsum,addition)

        return maxsum/k

        