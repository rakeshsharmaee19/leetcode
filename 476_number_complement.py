class Solution:
    def findComplement(self, num: int) -> int:
        a  = str(bin(num))[2:]
        for i in range(len(a)):
            if a[i] == '0':
                a = a[:i]+'1'+a[i+1:]
            else:
                a = a[:i]+'0'+a[i+1:]
        return int(a,2)
