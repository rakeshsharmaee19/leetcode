class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        mx= 0
        l = bottom
        special.sort()
        for idx, value in enumerate(special):
            if idx==0:
                mx=max(mx, value-l)
                l=value
            else:
                mx=max(mx, value-l-1)
                l=value
        mx=max(mx, top-value)
        return mx
