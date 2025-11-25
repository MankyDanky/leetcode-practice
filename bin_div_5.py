class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        res = []
        curr = 0
        for num in nums:
            curr<<=1
            curr^=num
            res.append(curr%5==0)
        return res