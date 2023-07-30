class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(set(nums))==len(nums):
            return len(nums)
        else:
            res=[]
            i=0
            while nums[i]!="_":
                if nums[i] in set(res):
                    nums.pop(i)
                    nums.append('_')
                else:
                    res.append(nums[i])
                    i+=1
            a =len(res)
            return a
