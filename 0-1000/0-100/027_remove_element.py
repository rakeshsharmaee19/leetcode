class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cp=0
        for i in range(len(nums)):
            if nums[i]!=val:
                if nums[cp]==val or nums[cp]=='_':
                    nums[cp], nums[i] = nums[i],nums[cp]
                cp+=1
            else:
                if nums[cp]!='_':
                    cp=i
                nums[i]='_'
        return cp
