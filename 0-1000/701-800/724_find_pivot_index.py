class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sm = sum(nums)
        lsm = 0
        for i in range(len(nums)):
            if i==0:
                lsm =0
            else:
                lsm+=nums[i-1]
            if lsm == sm-lsm-nums[i]:
                return i
        return -1
