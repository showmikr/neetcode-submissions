from itertools import chain, islice
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = list(accumulate(chain([1], islice(nums, len(nums) - 1)), lambda x, y: x * y))
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            prefixes[i] *= postfix
            postfix *= nums[i]
        return prefixes