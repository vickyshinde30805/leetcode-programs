import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq=Counter(nums)
        ''' result=sorted(f.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for i in range(k):
            ans.append(result[i][0])
        return ans'''
        # another method by heapq
        return heapq.nlargest(k,freq.keys(),key=freq.get)
        

      