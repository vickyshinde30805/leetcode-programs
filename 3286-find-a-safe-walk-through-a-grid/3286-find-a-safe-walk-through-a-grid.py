from heapq import heappush, heappop
from typing import List

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        INF = float('inf')
        dist = [[INF] * n for _ in range(m)]

        start = grid[0][0]
        dist[0][0] = start

        pq = [(start, 0, 0)]

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while pq:
            cost, r, c = heappop(pq)

            if cost > dist[r][c]:
                continue

            if (r, c) == (m-1, n-1):
                return cost < health

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < m and 0 <= nc < n:
                    newCost = cost + grid[nr][nc]

                    if newCost < dist[nr][nc]:
                        dist[nr][nc] = newCost
                        heappush(pq, (newCost, nr, nc))

        return False