class Solution:
    def stoneGame(self, piles):
        n=len(piles)
        dp=[[None]*n for i in range(n)]
        def solve(i,j):
            if i==j:
                return piles[i]
            if dp[i][j]!=None:
                return dp[i][j]
            left=piles[i]-solve(i+1,j)
            right=piles[j]-solve(i,j-1)
            dp[i][j]=max(left,right)
            return dp[i][j]
        return solve(0,n-1)>=0
            
       