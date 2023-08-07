class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res=[]
        for i in s:
            res.append(str(ord(i)-96))
        s=''.join(res)
        for _ in range(k):
            sm = 0
            for i in s:
                sm+=int(i)
            s=str(sm)
        return int(s)
