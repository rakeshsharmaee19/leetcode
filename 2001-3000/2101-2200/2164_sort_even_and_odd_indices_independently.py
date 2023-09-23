class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        i=0
        j=1
        n=len(nums)
        while i<n or j<n:
            k=i+2
            while k<n:
                if nums[i]>nums[k]:
                    nums[i],nums[k]=nums[k],nums[i]
                k+=2
            m=j+2
            while m<n:
                if nums[j]<nums[m]:
                    nums[j],nums[m]=nums[m],nums[j]
                m+=2
            i+=2
            j+=2
        return nums
