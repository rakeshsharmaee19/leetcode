class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in grid:
            l=0
            r=len(grid[0])-1
            ch=False
            while l<=r:
                mid=(l+r)>>1
                if i[mid]<0:
                    ch=True
                    r=mid-1
                else:
                    l=mid+1
            if ch:
                c+=(len(i)-l)       
        return c
