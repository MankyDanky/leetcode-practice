class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(heights[0], 0)]
        res = 0
        n = len(heights)
        for i in range(1, n):
            curr = (heights[i], i)
            while stack and heights[i] < stack[-1][0]:
                print(stack, curr)
                res = max(res, stack[-1][0] * (i - stack[-1][1]))
                curr = (heights[i], stack[-1][1])
                stack.pop()
            print(stack, curr)
            stack.append(curr)

        while stack:
            res = max(res, stack[-1][0] * (n - stack[-1][1]))
            print(res)
            stack.pop()
        return res
            

