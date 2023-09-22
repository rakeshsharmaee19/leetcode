class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        mx = max(arr)
        for i in range(n-1):
            if arr[i]==mx:
                mx = max(arr[i+1:])
                arr[i]=mx
            else:
                arr[i] = mx
        arr[-1] = -1
        return arr
