
class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:

        # Option 1: Buy items separately
        option1 = need1 * cost1 + need2 * cost2

        # Option 2: Buy type 3 items for both requirements
        option2 = max(need1, need2) * costBoth

        # Option 3: Buy type 3 for common requirements,
        # then buy remaining items separately
        option3 = min(need1, need2) * costBoth

        option3 += (need1 - min(need1, need2)) * cost1
        option3 += (need2 - min(need1, need2)) * cost2

        return min(option1, option2, option3)
