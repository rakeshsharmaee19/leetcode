class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n=len(arr)
        if n==1:
            return False
        else:
            left_peak = 0
            right_peak = n-1
            st = arr[0]
            ed = arr[n-1]
            od_l = arr[0]
            for i in range(1,n):
                if arr[i]>arr[i-1]:
                    left_peak = i
                elif arr[i]==arr[i-1]:
                    return False
                else:
                    break
            for i in range(n-2,-1,-1):
                if arr[i]>arr[i+1]:
                    right_peak = i
                elif arr[i]==arr[i+1]:
                    return False
                else:
                    break
            if right_peak==left_peak and left_peak!=0 and right_peak!=n-1:
                return True
            else:
                return False
            
                
        
