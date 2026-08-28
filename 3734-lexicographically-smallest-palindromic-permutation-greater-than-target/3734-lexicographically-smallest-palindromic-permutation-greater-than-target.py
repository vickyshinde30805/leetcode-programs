from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)

        cnt = Counter(s)

        odd = ""
        odd_cnt = 0
        for c in sorted(cnt):
            if cnt[c] & 1:
                odd_cnt += 1
                odd = c

        if odd_cnt > 1:
            return ""

        half_cnt = Counter()
        for c in cnt:
            half_cnt[c] = cnt[c] // 2

        m = n // 2
        prefix = []
        ans = ""

        def dfs(pos: int, tight: bool):
            nonlocal ans

            if ans:
                return

            if pos == m:
                left = "".join(prefix)
                cur = left + odd + left[::-1]
                if cur > target:
                    ans = cur
                return

            start = target[pos] if tight else 'a'

            for k in range(ord(start), ord('z') + 1):
                ch = chr(k)
                if half_cnt[ch] == 0:
                    continue

                half_cnt[ch] -= 1
                prefix.append(ch)

                dfs(pos + 1, tight and ch == target[pos])

                prefix.pop()
                half_cnt[ch] += 1

                if ans:
                    return

        dfs(0, True)
        return ans