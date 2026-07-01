from collections import deque

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # Step 1: Multi-source BFS
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy

                if 0 <= nx < n and 0 <= ny < n and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

        # Step 2: Check function
        def can(safe):
            if dist[0][0] < safe:
                return False

            q = deque([(0,0)])
            visited = [[False]*n for _ in range(n)]
            visited[0][0] = True

            while q:
                x, y = q.popleft()

                if (x, y) == (n-1, n-1):
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < n and 0 <= ny < n and
                        not visited[nx][ny] and
                        dist[nx][ny] >= safe):

                        visited[nx][ny] = True
                        q.append((nx, ny))

            return False

        # Step 3: Binary Search
        low = 0
        high = max(max(row) for row in dist)

        while low <= high:
            mid = (low + high) // 2

            if can(mid):
                low = mid + 1
            else:
                high = mid - 1

        return high