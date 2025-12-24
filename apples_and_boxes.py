class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        res = 0
        while apples > 0:
            apples -= capacity[res]
            res += 1
        return res