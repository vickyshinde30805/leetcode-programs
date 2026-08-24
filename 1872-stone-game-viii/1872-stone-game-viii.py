class Solution:
    def stoneGameVIII(self, stones):
        n = len(stones)
        
        # build prefix sum array
        prefix = [0] * n
        prefix[0] = stones[0]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + stones[i]
        
        # dp[i] collapses into a single rolling variable
        # since dp[i] only depends on dp[i+1]
        dp = prefix[n - 1]
        
        for i in range(n - 2, 0, -1):
            dp = max(dp, prefix[i] - dp)
        
        return dp