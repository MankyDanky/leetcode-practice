class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        stack = []
        n = len(rains)
        lakes = defaultdict(int)
        prev = defaultdict(int)
        res = [-1] * n
        for i in range(n):
            if rains[i] == 0:
                stack.append(i)
            else:
                lakes[rains[i]] += 1
                if lakes[rains[i]] > 1:
                    if not stack or stack[-1] < prev[rains[i]]:
                        return []
                    index = bisect.bisect_right(stack, prev[rains[i]])
                    p = stack.pop(index)
                    lakes[rains[i]] -= 1
                    res[p] = rains[i]
                prev[rains[i]] = i
        while stack:
            res[stack.pop()] = 1
        return res