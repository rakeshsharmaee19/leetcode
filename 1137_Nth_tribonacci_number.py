class Solution:
    def tribonacci(self, n: int) -> int:
        def memo(n, dp):
            if n<=2:
                return dp[n]
            if dp[n]!=-1:
                return dp[n]
            sm = memo(n-3,dp)+memo(n-2,dp)+memo(n-1,dp)
            dp[n]=sm
            return dp[n]
        if n<=2:
            dp=[0,1,1]
            return dp[n]
        dp=[-1]*(n+1)
        dp[0],dp[1],dp[2]=0,1,1
        return memo(n,dp)
