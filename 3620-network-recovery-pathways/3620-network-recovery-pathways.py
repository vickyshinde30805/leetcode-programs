from collections import deque
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        graph = [[] for _ in range(n)]
        indegree = [0] * n
        max_cost = 0

        for u, v, w in edges:
            graph[u].append((v, w))
            indegree[v] += 1
            max_cost = max(max_cost, w)

        # Topological order
        q = deque(i for i in range(n) if indegree[i] == 0)
        topo = []

        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

        INF = 10 ** 18

        def check(limit: int) -> bool:
            dp = [INF] * n
            dp[0] = 0

            for u in topo:
                if dp[u] == INF:
                    continue

                # Skip expanding from offline intermediate nodes
                if u != 0 and u != n - 1 and not online[u]:
                    continue

                for v, w in graph[u]:
                    if w < limit:
                        continue

                    # Destination can be offline only if it is n-1
                    if v != n - 1 and not online[v]:
                        continue

                    if dp[u] + w < dp[v]:
                        dp[v] = dp[u] + w

            return dp[n - 1] <= k

        lo, hi = 0, max_cost
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1

        return ans