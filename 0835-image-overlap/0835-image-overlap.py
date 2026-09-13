from collections import defaultdict

class Solution:
    def largestOverlap(self, img1, img2):
        n = len(img1)

        points1 = []
        points2 = []

        # Store coordinates of all 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))

                if img2[r][c] == 1:
                    points2.append((r, c))

        shifts = defaultdict(int)

        # Compare every 1 in img1 with every 1 in img2
        for r1, c1 in points1:
            for r2, c2 in points2:

                dr = r2 - r1
                dc = c2 - c1

                shifts[(dr, dc)] += 1

        return max(shifts.values(), default=0)