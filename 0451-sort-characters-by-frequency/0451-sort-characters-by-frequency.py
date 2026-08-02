from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq=Counter(s)
        result=sorted(freq.items(),key=lambda x:x[1],reverse=True)
        ans=""
        for ch ,count in (result):
            ans+=ch*count
        return ans

        