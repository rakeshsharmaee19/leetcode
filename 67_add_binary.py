class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>=len(b):
            b = '0'*(len(a)-len(b))+b
        else:
            a = '0'*(len(b)-len(a))+a
        carry = 0
        res = ''
        for i in range(len(a)-1,-1,-1):
            sm = int(a[i])+int(b[i])+carry
            if sm<=1:
                carry = 0
                res = str(sm)+res
            elif sm ==2:
                carry = 1
                res = '0'+res
            else:
                carry = 1
                res = '1'+res
        if carry:
            res='1'+res
        return res
