class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        if digits == [9] * n:
            return [1] + [0]*n
        else:
            carryover = 1
            for i in range(n-1, -1, -1):
                if digits[i] + carryover < 10:
                    digits[i] += carryover
                    break
                else:
                    digits[i] = 0
                    carryover = 1

            return digits