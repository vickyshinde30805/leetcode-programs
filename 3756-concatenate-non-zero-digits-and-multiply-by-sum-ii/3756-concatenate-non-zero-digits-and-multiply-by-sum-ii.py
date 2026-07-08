class Solution:
    def sumAndMultiply(self, s: str, queries):
        MOD = 10**9 + 7

        # Extract non-zero digits
        digits = []
        pos_to_idx = [-1] * len(s)

        for i, ch in enumerate(s):
            if ch != '0':
                pos_to_idx[i] = len(digits)
                digits.append(int(ch))

        m = len(digits)

        # Prefix digit sums
        prefix_sum = [0] * (m + 1)
        for i in range(m):
            prefix_sum[i + 1] = prefix_sum[i] + digits[i]

        # Powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # Prefix concatenation hash
        prefix_hash = [0] * (m + 1)
        for i in range(m):
            prefix_hash[i + 1] = (prefix_hash[i] * 10 + digits[i]) % MOD

        n = len(s)

        # prev_nonzero[i] = compressed index of last non-zero <= i
        prev_nonzero = [-1] * n
        last = -1
        for i in range(n):
            if pos_to_idx[i] != -1:
                last = pos_to_idx[i]
            prev_nonzero[i] = last

        # next_nonzero[i] = compressed index of first non-zero >= i
        next_nonzero = [-1] * n
        last = -1
        for i in range(n - 1, -1, -1):
            if pos_to_idx[i] != -1:
                last = pos_to_idx[i]
            next_nonzero[i] = last

        ans = []

        for l, r in queries:
            L = next_nonzero[l]
            R = prev_nonzero[r]

            if L == -1 or R == -1 or L > R:
                ans.append(0)
                continue

            digit_sum = prefix_sum[R + 1] - prefix_sum[L]

            length = R - L + 1
            x = (prefix_hash[R + 1] - prefix_hash[L] * pow10[length]) % MOD

            ans.append((x * digit_sum) % MOD)

        return ans