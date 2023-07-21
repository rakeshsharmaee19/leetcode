class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = int(''.join(str(i) for i in digits))
        return [int(i) for i in str(s+1)]
