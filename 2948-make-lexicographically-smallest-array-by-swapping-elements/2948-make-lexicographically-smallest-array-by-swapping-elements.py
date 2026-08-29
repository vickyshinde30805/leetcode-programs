class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)

        # (value, original_index)
        arr = sorted((num, i) for i, num in enumerate(nums))

        ans = [0] * n
        i = 0

        while i < n:
            j = i

            # Find one connected group
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Original indices in this group
            indices = sorted(arr[k][1] for k in range(i, j + 1))

            # Assign smallest values to smallest indices
            for k, idx in enumerate(indices):
                ans[idx] = arr[i + k][0]

            i = j + 1

        return ans