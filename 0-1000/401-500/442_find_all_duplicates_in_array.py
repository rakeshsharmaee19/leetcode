class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res_dict ={}
        re = []
        for i in range(1,n+1):
            res_dict[i] = None
        for i in nums:
            if res_dict[i]:
                re.append(i)
            else:
                res_dict[i]=1
        return re
        
