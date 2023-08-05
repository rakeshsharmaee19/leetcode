import math
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==2 or n==1:
            return True
        elif n==0:
            return False
        elif n&1!=0:
            return False
        else:
            if math.ceil(n/2)==n//2:
                n=n>>1
                a = self.isPowerOfTwo(n)
                return a
            else:
                return False
