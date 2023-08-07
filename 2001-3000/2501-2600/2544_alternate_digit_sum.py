class Solution:
    def alternateDigitSum(self, n: int) -> int:
        sm_e=0
        sm_o=0
        sn=str(n)
        for i in range(len(sn)):
            if i&1==0:
                sm_e+=int(sn[i])
            else:
                sm_o+=int(sn[i])
        return sm_e-sm_o
            
