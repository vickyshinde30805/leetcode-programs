class Solution:
    def isPalindrome(self, s: str) -> bool:
        n=len(s)
        l=0
        r=n-1
        while l<=r:
            left=s[l]
            right=s[r]
            if not left.isalnum():l+=1
            elif not right.isalnum():r-=1
            elif left.lower() != right.lower():
                return False
            else:
                l+=1
                r-=1
        return True


                

        