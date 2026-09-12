from bisect import bisect_right
from functools import lru_cache

class Solution:
    def maximumWeight(self, intervals):

        # [left, right, weight, original_index]
        arr = [
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by starting point
        arr.sort()

        n = len(arr)

        # All starting positions
        starts = [x[0] for x in arr]

        # next[i] = first interval that doesn't overlap with i
        nxt = [0] * n

        for i in range(n):
            right = arr[i][1]

            # Need next.left > current.right
            nxt[i] = bisect_right(starts, right)

        @lru_cache(None)
        def dp(i, k):

            # No intervals left OR already selected 4
            if i == n or k == 0:
                return (0, ())

            # ----------------
            # OPTION 1: SKIP
            # ----------------
            skip_score, skip_indices = dp(i + 1, k)

            # ----------------
            # OPTION 2: TAKE
            # ----------------
            take_score, take_indices = dp(nxt[i], k - 1)

            take_score += arr[i][2]

            take_indices = tuple(
                sorted(take_indices + (arr[i][3],))
            )

            # ----------------
            # CHOOSE BEST
            # ----------------

            # Higher score is better
            if take_score > skip_score:
                return (take_score, take_indices)

            if take_score < skip_score:
                return (skip_score, skip_indices)

            # Same score:
            # lexicographically smaller indices
            if take_indices < skip_indices:
                return (take_score, take_indices)

            return (skip_score, skip_indices)

        return list(dp(0, 4)[1])