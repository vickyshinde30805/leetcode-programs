class Solution:
    def sumCounts(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        sum_tree = [0] * (4 * n)
        square_tree = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, start, end, value):
            length = end - start + 1

            square_tree[node] += (
                2 * value * sum_tree[node]
                + value * value * length
            )

            sum_tree[node] += value * length
            lazy[node] += value

        def push(node, start, end):
            if lazy[node] == 0 or start == end:
                return

            mid = (start + end) // 2

            apply(node * 2, start, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, end, lazy[node])

            lazy[node] = 0

        def update(node, start, end, left, right):
            if right < start or end < left:
                return

            if left <= start and end <= right:
                apply(node, start, end, 1)
                return

            push(node, start, end)

            mid = (start + end) // 2

            update(node * 2, start, mid, left, right)
            update(node * 2 + 1, mid + 1, end, left, right)

            sum_tree[node] = (
                sum_tree[node * 2]
                + sum_tree[node * 2 + 1]
            )

            square_tree[node] = (
                square_tree[node * 2]
                + square_tree[node * 2 + 1]
            )

        last = {}
        answer = 0

        for i in range(n):
            prev = last.get(nums[i], -1)

            update(
                1,
                0,
                n - 1,
                prev + 1,
                i
            )

            answer = (answer + square_tree[1]) % MOD

            last[nums[i]] = i

        return answer