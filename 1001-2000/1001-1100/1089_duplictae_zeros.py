class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        
        n=len(arr)
        res=[0]*n
        i=j=0
        while i<n:
            if arr[j]==0:
                i+=2           
            else:
                res[i]=arr[j]
                i+=1
            j+=1
        arr.clear()
        arr.extend(res)
