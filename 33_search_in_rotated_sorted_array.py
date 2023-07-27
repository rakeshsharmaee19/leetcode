class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in set(nums):
            return nums.index(target)
        else:
            return -1
