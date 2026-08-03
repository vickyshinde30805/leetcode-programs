class Solution:
    r=["Bob","Tie","Alice"]
    def stoneGameIII(self, s: List[int]) -> str:
        n=len(s)
        
        @cache
        def solve(i):
            if i==n:return 0
            a=b=c=-5e7

            if i<n:
                a=s[i]-solve(i+1)
            if i+1<n:
                b=s[i]+s[i+1]-solve(i+2)
            if i+2<n:
                c=s[i]+s[i+1]+s[i+2]-solve(i+3)
            return max(a,b,c)

        b=solve(0)
        return self.r[(b>0)-(b<0)+1]
