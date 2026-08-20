class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left_ptr = 0
        res = len(nums) + 1
        running_sum = 0
        for right_ptr in range(len(nums)):
            running_sum += nums[right_ptr]
            if running_sum < target:
                continue
            while running_sum - nums[left_ptr] >= target:
                running_sum -= nums[left_ptr]
                left_ptr += 1
            res = min(right_ptr - left_ptr + 1, res)
        return res if res <= len(nums) else 0
            