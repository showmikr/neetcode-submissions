class Solution:
    def climbStairs(self, n: int) -> int:
        f0, f1 = 1, 1
        if n <= 1:
            return 1
        res = 0
        for i in range(2, n + 1):
            res = f0 + f1
            f0, f1 = f1, res
        return res

