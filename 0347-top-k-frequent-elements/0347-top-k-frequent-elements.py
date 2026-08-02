from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        result=sorted(freq.items(),key=lambda x: x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(result[i][0])
        return ans
        