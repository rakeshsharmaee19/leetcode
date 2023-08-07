class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        r=str(num)
        r1=str(int(r[::-1]))
        r2 = int(r1[::-1])
        return r2==num
