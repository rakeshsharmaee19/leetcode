class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        val = 0
        for i in range(1,11):
            dif = purchaseAmount-i*10
            if dif<=0:
                val=i*10
                break
        ans = val
        if (val-purchaseAmount)>5:
            ans-=10
        return 100-ans
