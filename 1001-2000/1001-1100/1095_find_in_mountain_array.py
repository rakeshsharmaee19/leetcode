# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n=mountain_arr.length()
        if n<3:
            return -1
        peak=self.findPeak(0, n-1, mountain_arr, n)
        index_left=True
        l=0
        first_end=peak
        second_start=peak+1
        second_end=n-1
        while l<=first_end:
            mid=(l+first_end)>>1
            mid_value=mountain_arr.get(mid)
            if mid_value==target:
                return mid
            elif mid_value<target:
                l=mid+1
            else:
                first_end=mid-1
        while second_start<=second_end:
            mid=(second_start+second_end)>>1
            mid_value=mountain_arr.get(mid)
            if mid_value==target:
                return mid
            elif mid_value<target:
                second_end=mid-1
            else:
                second_start=mid+1
        return -1

    def findPeak(self, l, r, mountain_arr, n):
        while l<=r:
            mid=(l+r)>>1
            value=mountain_arr.get(mid)
            if (mid==0 or value>mountain_arr.get(mid-1)) and ((mid==n-1) or value>mountain_arr.get(mid+1)):
                return mid
            elif value<mountain_arr.get(mid+1):
                l=mid+1
            else:
                r=mid-1
