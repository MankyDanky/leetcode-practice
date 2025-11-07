class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)
        left = 0
        power = [0] * n
        currPower = 0
        for right in range(n + r):
            if left < (right - 2*r):
                currPower -= stations[left]
                left += 1
            if (right < n):
                currPower += stations[right]
            if (right - r >= 0):
                power[right-r] = currPower

        def canMake(goal):
            rem = k
            updates = defaultdict(int)
            currAddition = 0
            for i in range(n):
                currAddition += updates[i]
                if power[i] + currAddition < goal:
                    diff = goal - power[i] - currAddition
                    if diff > rem:
                        return False
                    rem -= diff
                    updates[i + 2*r + 1] -= diff
                    currAddition += diff
                
            return True

        
        left = min(power)
        right = max(power) + k
        while left < right:
            mid = math.ceil((left+right)/2)
            if (canMake(mid)):
                left = mid
            else:
                right = mid - 1
        return left
