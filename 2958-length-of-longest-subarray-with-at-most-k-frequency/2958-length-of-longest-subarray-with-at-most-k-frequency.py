from collections import Counter
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        left=0
        ans=0
        f1=Counter()
        for right in range(len(nums)):

            f1[nums[right]]+=1
            while f1[nums[right]]>k:
                
                f1[nums[left]]-=1
                left+=1

            ans=max(ans,right-left+1)
            
        
        return ans
        


            



        


        