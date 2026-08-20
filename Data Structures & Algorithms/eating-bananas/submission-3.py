class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # isValidK runs in O(n) time
        eat_time = lambda eat_rate: sum(math.ceil(p / eat_rate) for p in piles)
        max_k = max(piles)
        l, r = 1, max_k
        mid = (l + r) // 2
        best_k = mid
        while l <= r:
            mid = (l + r) // 2
            time = eat_time(mid)
            if time <= h:
                best_k = mid
                r = mid - 1
            else:
                l = mid + 1
        return best_k
        





