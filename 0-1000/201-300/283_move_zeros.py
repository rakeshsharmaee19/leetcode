class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cp=0
        for i in range(len(nums)):
            if nums[i]!=0:
                if nums[cp]==0:
                    nums[cp], nums[i] = nums[i],nums[cp]
                cp+=1
            else:
                if nums[cp]!=0:
                    cp=i
