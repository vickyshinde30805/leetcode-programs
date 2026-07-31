from collections import Counter
class Solution:
    def minimumPushes(self, word: str) -> int:
        freq=Counter(word)
        arr=sorted(freq.values(),reverse=True)
        ans=0
        for i in range(len(arr)):
            pushes=(i//8)+1
            ans+=arr[i]*pushes
        return ans

        