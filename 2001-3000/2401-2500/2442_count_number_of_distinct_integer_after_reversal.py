class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n= len(nums)
        for i in range(n):
            aa = str(nums[i])
            nums.append(int(aa[::-1]))
        return len(set(nums))
