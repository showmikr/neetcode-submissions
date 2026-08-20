import heapq as hq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        freq_buckets = [[] for i in range(len(nums) + 1)]
        for n, freq in freq_map.items():
            freq_buckets[freq].append(n)
        res = []
        for bucket in (b for b in reversed(freq_buckets) if b):
            if len(res) >= k:
                break
            res.extend(bucket)
        return res
            
            
            
