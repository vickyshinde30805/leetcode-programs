import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f=Counter(nums)
        return heapq.nlargest(k,f.keys(),key=f.get)
       
        