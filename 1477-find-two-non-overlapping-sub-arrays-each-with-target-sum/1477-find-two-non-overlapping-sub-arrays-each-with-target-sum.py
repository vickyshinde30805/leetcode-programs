class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)

        INF = float('inf')

        best = [INF] * n
        left = 0
        curr_sum = 0

        ans = INF
        min_len = INF

        for right in range(n):
            curr_sum += arr[right]

            # Shrink window if sum becomes greater than target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            # Valid subarray found
            if curr_sum == target:
                length = right - left + 1

                # If another valid subarray exists before this
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                min_len = min(min_len, length)

            best[right] = min_len

        return -1 if ans == INF else ans