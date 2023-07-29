class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nm=1
        c=0
        s=[]
        while c<k:
            if nm not in set(arr):
                s.append(nm)
                c+=1
            nm+=1
        return s[-1]
            
