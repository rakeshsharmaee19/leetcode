class Solution:
    def sumOfMultiples(self, n: int) -> int:
            
        def sumnum(num, d):
            return ((num*d*(num+1))/2)

        sum3 = sumnum((n//3), 3)
        sum5 = sumnum((n//5), 5)
        sum7 = sumnum((n//7), 7)
        sum15 = sumnum((n//15), 15)
        sum21 = sumnum((n//21), 21)
        sum35 = sumnum((n//35), 35)
        sum105 = sumnum((n//105), 105)
        return int((sum3+sum5+sum7 -sum15 -sum21 - sum35 +sum105))
