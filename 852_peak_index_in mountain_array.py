class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        a = max(arr)
        return arr.index(a)
