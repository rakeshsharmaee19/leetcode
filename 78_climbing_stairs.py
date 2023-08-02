class Solution:
    def memo(self,n, arr):
        if n<=1:
            return 1
        if arr[n]!=-1:
            return arr[n]
        sm = self.memo(n-1, arr)+self.memo(n-2, arr)
        arr[n]=sm
        return arr[n]
    def climbStairs(self, n: int) -> int:
        dp = [-1]*(n+2)
        return self.memo(n, dp)
