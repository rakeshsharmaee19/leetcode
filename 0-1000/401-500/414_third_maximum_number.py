class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # print(e-21)
        fm=-e**31
        sm=-e**31
        tm=-e**31
        ch=0
        for i in nums:
            if i>=fm:
                if i!=fm:
                    ch+=1
                    tm=sm
                    sm=fm
                    fm=i
            elif i<fm and i>=sm:
                if i!=sm:
                    ch+=1
                    tm=sm
                    sm=i
            else:
                if i!=tm and tm<i:
                    ch+=1
                    tm=i
        if ch<3:
            return fm
        else:
            return tm
