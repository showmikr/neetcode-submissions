class Solution:
    def climbStairs(self, n: int) -> int:
        f1, f2 = 1, 2
        if n == 1:
            return f1
        if n == 2:
            return f2
        res = 0
        for i in range(3, n + 1):
            res = f1 + f2
            f1, f2 = f2, res
        return res

