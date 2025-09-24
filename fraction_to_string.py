class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        
        fraction = ""

        if (numerator < 0) != (denominator < 0):
            fraction = "-"

        dividend = abs(numerator)
        divisor = abs(denominator)

        fraction += str(dividend // divisor)
        remainder = dividend % divisor
        if remainder == 0:
            return fraction
        
        fraction += "."

        seen = {}

        while remainder != 0:
            if remainder in seen:
                fraction = fraction[:seen[remainder]] + "(" + fraction[seen[remainder]:]
                fraction += ")"
                return fraction
            seen[remainder] = len(fraction)
            remainder *= 10
            fraction += str(remainder // divisor)
            remainder %= divisor
        return fraction