import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            heaviest = -heapq.heappop(stones)
            secondHeaviest = -heapq.heappop(stones)
            if heaviest == secondHeaviest:
                continue
            else:
                heapq.heappush(stones, -1*abs(heaviest - secondHeaviest))
        return 0 if len(stones) == 0 else -stones[0]