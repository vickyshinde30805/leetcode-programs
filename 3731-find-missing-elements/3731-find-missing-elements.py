class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        m=min(nums)
        mx=max(nums)
        ans=[]
        if mx-m+1==len(nums):
            return []

        for i in range(m,mx+1):
            if i not in nums:
                ans.append(i)

        ans.sort()
        return ans
        
        
        
            