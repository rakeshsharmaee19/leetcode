class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        check=True 
        while check:
            if original in nums:
                original = original*2
            else:
                check=False
        return original
        
