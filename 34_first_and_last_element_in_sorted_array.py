class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        c = nums.count(target)
        try:
            i = nums.index(target)
        except:
            return [-1, -1]
        return [i, i+c-1]
