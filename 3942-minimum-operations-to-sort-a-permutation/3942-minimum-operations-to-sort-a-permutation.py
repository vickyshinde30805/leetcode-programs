class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        # Position of 0
        zero = nums.index(0)

        def check(step):
            for i in range(1, n):
                prev = (zero + (i - 1) * step) % n
                curr = (zero + i * step) % n

                if nums[prev] > nums[curr]:
                    return False

            return True

        ans = float('inf')

        # Case 1: nums is cyclically increasing
        if check(1):
            # Directly rotate left
            ans = min(ans, zero)

            # Reverse -> rotate -> reverse
            ans = min(ans, n - zero + 2)

        # Case 2: nums is cyclically decreasing
        if check(-1):
            # Rotate -> reverse
            ans = min(ans, zero + 2)

            # Reverse -> rotate
            ans = min(ans, n - zero)

        if ans == float('inf'):
            return -1

        return ans