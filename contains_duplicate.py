class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        check=False
        i=0
        d={}
        n=len(nums)
        while check==False and i<n:
            if nums[i] in d:
                check=True
            else:
                d[nums[i]]=1
            i=i+1
        return check
