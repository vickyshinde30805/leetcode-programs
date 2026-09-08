class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        k = 1

        while True:
            start = 10 ** (3 * k)
            if start > n:
                break

            end = 10 ** (3 * (k + 1)) - 1
            cnt = min(n, end) - start + 1
            ans += cnt * k
            k += 1

        return ans