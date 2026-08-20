class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        interim_solutions = [amount + 1 for _ in range(amount + 1)]        
        interim_solutions[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if amount - c >= 0:
                    interim_solutions[i] = min(interim_solutions[i], interim_solutions[i - c] + 1)
        return interim_solutions[amount] if interim_solutions[amount] < amount + 1 else -1
