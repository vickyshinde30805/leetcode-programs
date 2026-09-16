class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # We need C(n + k - 1, 2k)
        N = n + k - 1
        R = 2 * k

        # Calculate nCr using factorials
        fact = [1] * (N + 1)

        for i in range(1, N + 1):
            fact[i] = fact[i - 1] * i % MOD

        # Fermat's Little Theorem:
        # inverse(a) = a^(MOD-2) % MOD
        def mod_inverse(a):
            return pow(a, MOD - 2, MOD)

        numerator = fact[N]
        denominator = (
            fact[R] *
            fact[N - R]
        ) % MOD

        return numerator * mod_inverse(denominator) % MOD