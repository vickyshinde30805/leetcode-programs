
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Count items having each factor
        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count how many other items each factor can unlock
        for i in range(1, n + 1):
            for j in range(i * 2, n + 1, i):
                freq[i] += freq[j]

        # Minimum item price
        min_price = min(price for factor, price in items)

        # Process cheaper bonus items first
        items.sort(key=lambda x: x[1])

        ans = 0

        for factor, price in items:
            if price >= 2 * min_price:
                break

            # Number of free copies available for this item type
            gain = freq[factor] - 1

            if gain <= 0:
                continue

            # Buy as many bonus copies as possible
            take = min(gain, budget // price)

            ans += take * 2
            budget -= take * price

        # Spend remaining budget on cheapest items
        ans += budget // min_price

        return ans
