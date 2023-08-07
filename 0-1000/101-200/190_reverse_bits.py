class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)
        b=str(a[:1:-1])+'0'*32
        nm = int(b[:32],2)
        return nm
