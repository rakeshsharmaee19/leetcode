class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        cp=0
        for i in range(len(nums)):
            if nums[i]%2==0:
                if nums[cp]%2!=0:
                    nums[cp], nums[i] = nums[i],nums[cp]
                cp+=1
            else:
                if nums[cp]%2==0:
                    cp=i
        return nums
