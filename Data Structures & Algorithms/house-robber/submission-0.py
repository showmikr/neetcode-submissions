class Solution:
    def rob(self, nums: List[int]) -> int:
        rob_i, rob_j = 0, nums[0] 
        for i in range(1, len(nums)):
            best_rob = max(rob_i + nums[i], rob_j)
            rob_i, rob_j = rob_j, best_rob
        return rob_j
