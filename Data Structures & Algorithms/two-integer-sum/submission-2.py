class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prefixes = dict()
        for i, n in enumerate(nums):
            pfx = target - n
            if pfx in prefixes:
                return [prefixes[pfx], i]
            prefixes[n] = i
        return  [0, 0]

        