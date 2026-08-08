class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        ans=[]

        count_p=[0]*26
        count_s=[0]*26

        for i in range(len(p)):
            count_p[ord(p[i])-ord('a')]+=1
            count_s[ord(s[i])-ord('a')]+=1

        if count_p==count_s:
            ans.append(0)
        for i in range(len(p),len(s)):
            count_s[ord(s[i])-ord('a')]+=1
            count_s[ord(s[i-len(p)])-ord('a')]-=1

            if count_p==count_s:
                ans.append(i-len(p)+1)

        return ans


        
        
        



