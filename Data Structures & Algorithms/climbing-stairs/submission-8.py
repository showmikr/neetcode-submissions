class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # assuming n > 2
        n_minus_one, n_minus_two = 1, 1
        for i in range(3, n + 1):
            new_n = n_minus_one + n_minus_two
            n_minus_one, n_minus_two = new_n, n_minus_one
        return n_minus_one + n_minus_two
