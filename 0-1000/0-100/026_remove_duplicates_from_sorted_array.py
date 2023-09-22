class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        insert_position = 1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[insert_position] = nums[i]
                insert_position+=1
        return insert_position
