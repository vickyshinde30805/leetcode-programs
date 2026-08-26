class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        l = 0
        ones = 0
        ans = ""

        for r in range(n):
            if s[r] == '1':
                ones += 1

            while ones > k:
                if s[l] == '1':
                    ones -= 1
                l += 1

            if ones == k:
                # Remove unnecessary leading zeros
                while s[l] == '0':
                    l += 1

                cur = s[l:r + 1]

                if (not ans or
                    len(cur) < len(ans) or
                    (len(cur) == len(ans) and cur < ans)):
                    ans = cur

                # Move past the leftmost '1'
                ones -= 1
                l += 1

        return ans