import itertools
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res= [[]]
        for i in range(1,len(nums)+1):
            com_set = itertools.combinations(nums, i)
            for val in com_set:
                res.append(val)
        return res
