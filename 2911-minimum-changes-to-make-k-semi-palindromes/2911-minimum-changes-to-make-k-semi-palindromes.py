
from typing import List

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # cost[i][j] = minimum changes to make s[i:j+1]
        # a semi-palindrome
        cost = [[INF] * n for _ in range(n)]

        # Precompute the cost of every substring
        for i in range(n):
            for length in range(2, n - i + 1):
                j = i + length - 1
                best = INF

                # Try every proper divisor of the length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0
                    group_size = length // d

                    # Check each repeating-pattern group
                    for r in range(d):
                        left = i + r
                        right = i + r + (group_size - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[i][j] = best

        # DP: dp[p][i] = minimum changes to divide
        # first i characters into p semi-palindromes
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):
                for j in range(2 * (p - 1), i - 1):
                    if dp[p - 1][j] != INF:
                        dp[p][i] = min(
                            dp[p][i],
                            dp[p - 1][j] + cost[j][i - 1]
                        )

        return dp[k][n]
