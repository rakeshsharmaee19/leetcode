class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        if len(arr)==1:
            return 0
        while left<=right:
            mid=(left+right)>>1
            if (mid==0 or arr[mid]>=arr[mid-1] ) and (mid==len(arr)-1 or arr[mid]>=arr[mid+1]) :
                return mid
            elif arr[mid]<=arr[mid+1]:
                left=mid+1
            else:
                right=mid-1
        return -1
