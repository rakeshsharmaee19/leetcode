import math
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if len(dist)>math.ceil(hour):
            return -1
        else:
            right= ceil(max(max(dist),dist[-1]/(1 if hour.is_integer() else hour-int(hour))))
            left = max(1,int(sum(dist)/math.ceil(hour)))
            while left<right:
                mid = (left+right)//2
                sm = 0
                for i in dist[:len(dist)-1]:
                    sm+=math.ceil(i/mid)
                sm+=dist[-1]/mid
                if sm<=hour:
                    right=mid
                else:
                    left=mid+1
            return left
