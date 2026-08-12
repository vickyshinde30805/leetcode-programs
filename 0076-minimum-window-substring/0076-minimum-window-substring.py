from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        freq=Counter(t)
        left=0
        need=len(t)

        start =0
        min_len=float('inf')

        for right in range(len(s)):
            if freq[s[right]]>0:
                need-=1
            freq[s[right]]-=1

            while need==0:
                if right-left+1< min_len:
                    min_len=right-left+1
                    start=left
                freq[s[left]]+=1

                if freq[s[left]]>0:
                    need+=1
                left+=1

        if min_len==float("inf"):
            return ""
        
        return s[start:start+min_len]


        
            

                
                
                
        