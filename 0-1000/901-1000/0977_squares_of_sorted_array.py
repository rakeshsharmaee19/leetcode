class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        mn=0
        mnval=abs(nums[0])
        res=[]
        for i in range(len(nums)):
            if abs(nums[i])<mnval:  #To find minimum Value index
                mn=i
                mnval=abs(nums[i])
            nums[i]=nums[i]**2
        k=mn-1
        j=mn+1
        res.append(nums[mn])

        while k>=0 or j<=i:
            if k>=0 and j<=i:
                if nums[k]<nums[j]:
                    res.append(nums[k])
                    k-=1
                else:
                    res.append(nums[j])
                    j+=1
            elif k>=0:
                res.append(nums[k])
                k-=1
            else:
                res.append(nums[j])
                j+=1
        return res
