class Solution:
    def smallestPalindrome(self, s: str) -> str:
        from collections import Counter
        
        freq = Counter(s)
        
        half = []
        middle = ""
        
        # Sort characters to ensure lexicographic order
        for ch in sorted(freq.keys()):
            count = freq[ch]
            
            # Add half of characters
            half.append(ch * (count // 2))
            
            # If odd count, store middle character
            if count % 2 == 1:
                middle = ch
        
        first_half = "".join(half)
        
        # Build palindrome
        return first_half + middle + first_half[::-1]