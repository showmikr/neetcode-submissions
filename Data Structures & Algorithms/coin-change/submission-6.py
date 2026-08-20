from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amnt):
            if amnt == 0:
                return 0
            res = amount + 1
            for c in coins:
                if amnt - c >= 0:
                    res = min(res, dfs(amnt - c) + 1)
            return res
        res = dfs(amount)
        return res if res < amount + 1 else -1




        