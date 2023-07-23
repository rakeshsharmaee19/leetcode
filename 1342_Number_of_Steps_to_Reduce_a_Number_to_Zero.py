class Solution:
    def numberOfSteps(self, num: int) -> int:
        st = 0
        while num!=0:
            if num&1==0:
                num=num>>1
            else:
                num = num-1
            st+=1
        return st
