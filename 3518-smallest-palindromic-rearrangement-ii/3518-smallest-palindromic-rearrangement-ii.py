from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        freq = Counter(s)

        chars = sorted(freq.keys())
        cnt = [freq[c] // 2 for c in chars]

        middle = ""
        for c in chars:
            if freq[c] & 1:
                middle = c

        total = sum(cnt)

        # Compute multinomial only once
        ways = factorial(total)
        for x in cnt:
            ways //= factorial(x)

        if ways < k:
            return ""

        ans = []

        while total:
            for i, ch in enumerate(chars):
                if cnt[i] == 0:
                    continue

                child = ways * cnt[i] // total

                if child >= k:
                    ans.append(ch)
                    ways = child
                    cnt[i] -= 1
                    total -= 1
                    break
                else:
                    k -= child

        left = "".join(ans)
        return left + middle + left[::-1]