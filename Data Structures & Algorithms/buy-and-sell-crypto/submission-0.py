from itertools import islice
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        best_min = prices[0]
        for p in islice(prices,1,len(prices)):
            max_profit = max(max_profit, p - best_min)
            best_min = min(best_min, p)
        return max_profit

        