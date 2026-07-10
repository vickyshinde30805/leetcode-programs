from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        # Sort by value
        arr = sorted((nums[i], i) for i in range(n))
        values = [x[0] for x in arr]

        # rank[original_index] = position in sorted order
        rank = [0] * n
        for pos, (_, idx) in enumerate(arr):
            rank[idx] = pos

        # nextRight[i] = farthest index reachable in one step
        nextRight = [0] * n
        j = 0
        for i in range(n):
            while j + 1 < n and values[j + 1] - values[i] <= maxDiff:
                j += 1
            nextRight[i] = j

        # Binary lifting
        LOG = n.bit_length()
        up = [nextRight]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(n)])

        ans = []

        for u, v in queries:
            ru = rank[u]
            rv = rank[v]

            if ru == rv:
                ans.append(0)
                continue

            if ru > rv:
                ru, rv = rv, ru

            if nextRight[ru] == ru:
                ans.append(-1)
                continue

            cur = ru
            steps = 0

            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < rv:
                    cur = nxt
                    steps += 1 << k

            if nextRight[cur] < rv:
                ans.append(-1)
            else:
                ans.append(steps + 1)

        return ans