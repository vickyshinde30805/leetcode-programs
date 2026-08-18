class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k==n:
            return max(nums)

        counter={}
        for x in nums:
            counter[x]=counter.get(x,0)+1

        if k==1:
            ans=-1
            for i in counter:
                if counter[i]==1:
                    ans=max(ans,i)
            return ans
        ans=-1
        if counter[nums[0]]==1:
            ans=max(ans,nums[0])
        if counter[nums[-1]]==1:
            ans=max(ans,nums[-1])
        return ans

        
    

        