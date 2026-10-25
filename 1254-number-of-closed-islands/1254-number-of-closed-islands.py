class Solution:
    def closedIsland(self, grid):
        m = len(grid)
        n = len(grid[0])

        def dfs(r, c):
            # Outside grid -> island touches boundary
            if r < 0 or r >= m or c < 0 or c >= n:
                return False

            # Water or already visited
            if grid[r][c] == 1:
                return True

            # Mark land as visited
            grid[r][c] = 1

            # Check all 4 directions
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up and down and left and right

        count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        count += 1

        return count