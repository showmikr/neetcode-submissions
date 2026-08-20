class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower_bound, upper_bound = 0, len(nums)
        while lower_bound < upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            res = nums[midpoint]
            if target < res:
                upper_bound = midpoint
            elif target > res:
                lower_bound = midpoint + 1
            else:
                return midpoint
        return -1
            

