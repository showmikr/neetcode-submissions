class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] 
        nums.sort()
        interim = []
        min_nums = min(nums)
        def dfs(tg: int, num_idx: int) -> None:
            if tg < 0:
                return
            if tg == 0:
                res.append([x for x in interim])
                return
            for i in range(num_idx, len(nums)):
                interim.append(nums[i])
                dfs(tg - nums[i], i)
                interim.pop()
        dfs(target, 0)
        return res
                 

