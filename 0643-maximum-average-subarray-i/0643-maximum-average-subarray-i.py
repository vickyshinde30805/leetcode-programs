class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        totalsum=0
        for i in range(k):
            totalsum+=nums[i]
        maxsum=totalsum
        for i in range(k,len(nums)):
            totalsum+=nums[i]
            totalsum-=nums[i-k]

            maxsum=max(maxsum,totalsum)
        
        return maxsum/k
        