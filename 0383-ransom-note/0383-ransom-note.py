from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        freq=Counter(magazine)
        freq_1=Counter(ransomNote)

        for char in ransomNote:
            if char in magazine and freq_1<=freq:

                return True
        return False
        
        