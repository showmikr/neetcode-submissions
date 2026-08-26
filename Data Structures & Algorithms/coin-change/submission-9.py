from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def cc(amnt):
            if amnt == 0:
                return 0
            if amnt < 0:
                return amount + 1
            res = amount + 1
            for c in coins:
                res = min(res, cc(amnt - c) + 1)
            return res
        res = cc(amount)
        return res if res < amount + 1 else -1