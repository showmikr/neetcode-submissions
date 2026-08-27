class Solution:
    def climbStairs(self, n: int) -> int:
        # this is where we derive the recurrence relation
        # but don't actually use
        def dfs(step):
            if step > n:
                return 0
            if step == n:
                return 1
            return sum(dfs(step + x) for x in [1,2])
        # this is where we use the recurrence relation:
        # dfs(step_x) = dfs(step_x + 1) + dfs(step_x + 2)
        step_x_plus_one = 1
        step_x_plus_two = 1
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        for i in reversed(range(0, n - 2)):
            res = step_x_plus_one + step_x_plus_two
            step_x_plus_one, step_x_plus_two = res, step_x_plus_one
        return step_x_plus_one + step_x_plus_two
