class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findPivot(nums: List[int]) -> int:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = (l + r) // 2
                lookup = nums[mid]
                if lookup <= nums[-1]:
                    r = mid - 1
                else:
                    l = mid + 1
            return l

        def binarySearch(l: int, r: int) -> int:
            while l <= r:
                mid = (l + r) // 2
                lookup = nums[mid]
                if lookup == target:
                    return mid
                elif lookup < target:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        pivot = findPivot(nums)
        answer = binarySearch(0, pivot - 1)
        if answer == -1:
            return binarySearch(pivot, len(nums) - 1)
        else:
            return answer

                

