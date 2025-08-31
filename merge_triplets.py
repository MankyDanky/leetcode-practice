class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cur = [float("-inf")] * 3
        for ai, bi, ci in triplets:
            if ai > target[0] or bi > target[1] or ci > target[2]:
                continue
            cur[0] = max(cur[0], ai)
            cur[1] = max(cur[1], bi)
            cur[2] = max(cur[2], ci)
        return cur == target