class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # check the len
        if len(s1)>len(s2):
            return False
        
        count1=[0]*26
        count2=[0]*26

        # for the first window
        for i in range(len(s1)):
            count1[ord(s1[i])-ord('a')]+=1
            count2[ord(s2[i])-ord('a')]+=1
        if count1==count2:
            return True
        
        #slide the window

        for i in range(len(s1),len(s2)):

            count2[ord(s2[i])-ord('a')]+=1
            count2[ord(s2[i-len(s1)])-ord('a')]-=1
            if count1==count2:
                return True
        return False