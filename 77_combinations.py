import itertools
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = [i for i in range(1,n+1)]
        res = []
        if n==1:
            return [[1]]
        else:
            perm_set = itertools.combinations(arr,k)
            for i in perm_set:
                res.append(i)
            return res
