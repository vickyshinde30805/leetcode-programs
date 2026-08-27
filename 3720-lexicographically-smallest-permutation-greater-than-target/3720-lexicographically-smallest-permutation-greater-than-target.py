from functools import lru_cache

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord('a')] += 1

        @lru_cache(None)
        def dfs(idx, state):
            if idx == len(target):
                return None  # equal to target, not strictly greater

            cnt = list(state)
            t = ord(target[idx]) - ord('a')

            # Try matching target character
            if cnt[t]:
                cnt[t] -= 1
                res = dfs(idx + 1, tuple(cnt))
                if res is not None:
                    return chr(t + 97) + res
                cnt[t] += 1

            # Try the smallest larger character
            for c in range(t + 1, 26):
                if cnt[c]:
                    cnt[c] -= 1
                    ans = [chr(c + 97)]
                    for k in range(26):
                        ans.append(chr(k + 97) * cnt[k])
                    return "".join(ans)

            return None

        ans = dfs(0, tuple(cnt))
        return "" if ans is None else ans