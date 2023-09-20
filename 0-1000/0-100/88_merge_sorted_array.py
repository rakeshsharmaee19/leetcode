class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        check=m+n-1  # index of nums1
        i = m-1
        j = n-1
        while (i>=0 or j>=0) and check>=0:
            if i>=0 and j>=0:
                if nums1[i]<nums2[j]:
                    nums1[check]=nums2[j]
                    j-=1
                    check-=1
                else:
                    nums1[check]=nums1[i]
                    i-=1
                    check-=1
            elif i>=0:
                check-=1
            else:
                nums1[check]=nums2[j]
                j-=1
                check-=1
