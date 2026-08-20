from itertools import islice

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = dict()
        for i, n in enumerate(nums):
            complement = target - n
            if complement in complements:
                return [complements[complement], i]
            complements[n] = i

        return [0, 0] # Should never reach given problem conditions
