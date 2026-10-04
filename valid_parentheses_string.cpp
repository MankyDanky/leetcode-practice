class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin = 0
        leftMax = 0
        for c in s:
            if c == '(':
                leftMin += 1
                leftMax += 1
            elif c == ')':
                leftMin -= 1
                leftMax -= 1
                if leftMax < 0:
                    return False
                leftMin = max(0, leftMin)
            else:
                leftMin = max(0, leftMin - 1)
                leftMax += 1
        return leftMin == 0
