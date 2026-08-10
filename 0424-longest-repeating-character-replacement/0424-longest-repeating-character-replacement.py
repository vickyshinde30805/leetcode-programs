class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=[0]*26
        left=0
        maxf=0
        res=0
        for right in range(len(s)):
            count[ord(s[right])-ord('A')]+=1
            maxf=max(maxf,count[ord(s[right])-ord('A')])

            if (right-left+1)-maxf >k:
                count[ord(s[left])-ord('A')]-=1
                left+=1
            
            res=max(res,right-left+1)
        return res
        
       
        