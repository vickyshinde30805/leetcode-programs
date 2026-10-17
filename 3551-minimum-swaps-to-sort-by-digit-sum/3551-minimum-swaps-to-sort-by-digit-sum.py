class Solution:
    def minSwaps(self, nums):
        # Calculate digit sum
        def digit_sum(n):
            total = 0
            while n > 0:
                total += n % 10
                n //= 10
            return total

        # Create the sorted version
        sorted_nums = sorted(nums, key=lambda x: (digit_sum(x), x))

        # Map each value to its correct position
        pos = {value: i for i, value in enumerate(sorted_nums)}

        swaps = 0
        visited = [False] * len(nums)

        # Find cycles
        for i in range(len(nums)):
            if visited[i] or pos[nums[i]] == i:
                continue

            cycle_size = 0
            j = i

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            swaps += cycle_size - 1

        return swaps
        