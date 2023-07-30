class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        while val in set(nums):
            idx = nums.index(val)
            nums.pop(idx)
            nums.append('_')
            count+=1
        return len(nums)-count
