
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        # prefix maximum
        pref_max = [0] * (n + 1)

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # suffix minimum
        INF = 10**9
        suff_min = [INF] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # prefix count of normal decreases
        drops = [0] * n

        for i in range(1, n):
            drops[i] = drops[i - 1]

            if nums[i - 1] > nums[i]:
                drops[i] += 1

        # check whether k is sortable
        def check(k):
            for start in range(0, n, k):
                end = start + k - 1

                # Number of decreases inside this block
                count = drops[end] - drops[start]

                # Check circular connection:
                # last element -> first element
                if nums[end] > nums[start]:
                    count += 1

                # A block must have at most one circular decrease
                if count > 1:
                    return False

                # Everything before this block must be
                # <= everything from this block onward
                if pref_max[start] > suff_min[start]:
                    return False

            return True

        answer = 0

        # Find all divisors of n
        k = 1

        while k * k <= n:
            if n % k == 0:

                if check(k):
                    answer += k

                other = n // k

                if other != k and check(other):
                    answer += other

            k += 1

        return answer