class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        a = str(bin(x))[2:]
        b = str(bin(y))[2:]
        if len(a)>len(b):
            b = '0'*(len(a)-len(b)) + b
        else:
            a = '0'*(len(b)-len(a)) + a
        count = 0
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return count
