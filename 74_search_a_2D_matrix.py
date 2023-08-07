class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
        mid_r=len(matrix[0])-1
        mid_l=0
        while l<=r:
            mid = (l+r)>>1
            if matrix[mid][0]<=target and matrix[mid][mid_r]>=target:
                while mid_l<=mid_r:
                    mid_mid=(mid_r+mid_l)>>1
                    if matrix[mid][mid_mid]==target:
                        return True
                    elif matrix[mid][mid_mid]<target:
                        mid_l=mid_mid+1
                    else:
                        mid_r=mid_mid-1
                return False
            elif matrix[mid][0]<target:
                l=mid+1
            else:
                r=mid-1
        return False
