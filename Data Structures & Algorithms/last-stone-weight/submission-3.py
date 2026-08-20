import heapq as hq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        for i in range(len(stones)):
            stones[i] = -stones[i]
        hq.heapify(stones)
        while len(stones) > 1:
            roids = [-hq.heappop(stones) for _ in range(2)]
            if roids[0] == roids[1]:
                continue
            hq.heappush(stones, -abs(roids[0] - roids[1]))
        return -stones[0] if stones else 0

        