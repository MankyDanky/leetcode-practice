class Solution:
    def smallestNumber(self, n: int) -> int:
        r = n.bit_length()
        return (1<<r)-1