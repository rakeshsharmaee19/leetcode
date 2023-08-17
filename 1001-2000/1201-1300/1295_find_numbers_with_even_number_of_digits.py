class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if (i>=10 and i<=99) or (i>=1000 and i<=9999) or i==100000:
                c+=1
        return c
