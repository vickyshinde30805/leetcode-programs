from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq=Counter(words)
        res=sorted(freq.items(),key=lambda x:(-x[1],x[0]))
        ans=[]
        for i in range(k):
            ans.append(res[i][0])
        return ans 