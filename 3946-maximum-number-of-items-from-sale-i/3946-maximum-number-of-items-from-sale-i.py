from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)

        dp = [0] * (budget + 1)

        for factor, price in items:
            free_count = sum(
                f % factor == 0 for f, p in items
            )

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + free_count)

        ans = 0

        for j in range(budget + 1):
            ans = max(ans, dp[j] + (budget - j) // min_price)

        return ans