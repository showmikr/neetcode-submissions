from functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def dfs(amnt):
            if amnt < 0:
                return float('inf')
            elif amnt == 0:
                return 0
            else:
                return min(dfs(amnt - c) for c in coins) + 1
        val = dfs(amount)
        return val if val < float('inf') else -1