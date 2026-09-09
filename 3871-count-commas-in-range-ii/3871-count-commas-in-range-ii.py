class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        commas = 1
        start = 1000  # 10^3

        while start <= n:
            end = start * 1000 - 1
            cnt = min(n, end) - start + 1
            ans += cnt * commas

            commas += 1
            start *= 1000

        return ans