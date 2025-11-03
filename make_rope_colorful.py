class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        j = 0
        n = len(neededTime)
        res = 0
        while j < n:
            maxTime = neededTime[j]
            totalTime = neededTime[j]
            color = colors[j]
            while j+1 < n and colors[j+1] == color:
                j += 1
                maxTime = max(maxTime, neededTime[j])
                totalTime += neededTime[j]
            res += totalTime - maxTime
            j += 1
        return res