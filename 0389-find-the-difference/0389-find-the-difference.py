from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cs=Counter(s)
        ct=Counter(t)

        for ch in t:
            if ct[ch]!=cs[ch]:
                return ch