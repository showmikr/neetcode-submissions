import heapq as hq
from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        for n in nums:
            freq_map[n] += 1
        values = [(-val, key) for key, val in freq_map.items()]
        hq.heapify(values)
        return [hq.heappop(values)[1] for _ in range(k)]
