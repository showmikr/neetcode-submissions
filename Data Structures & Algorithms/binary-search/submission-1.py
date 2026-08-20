class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower, upper = 0, len(nums) - 1
        while lower <= upper:
            mid = (upper + lower) // 2
            val = nums[mid]
            if target > val:
                lower = mid + 1
            elif target < val:
                upper = mid - 1
            else:
                return mid
        return -1

        
