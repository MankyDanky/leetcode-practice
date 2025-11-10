class Solution:
    def minOperations(self, nums: List[int]) -> int:
        cost = Counter(nums)
        stack = []
        for num in nums:
            if not stack or num >= stack[-1]:
                stack.append(num)
            else:
                while stack and num < stack[-1]:
                    top = stack[-1]
                    l = len(stack) - bisect.bisect_left(stack, top)
                    cost[top] -= l - 1
                    while stack and stack[-1] == top:
                        stack.pop()
                stack.append(num)

        while stack:
            top = stack[-1]
            l = len(stack) - bisect.bisect_left(stack, top)
            cost[top] -= l - 1
            while stack and stack[-1] == top:
                stack.pop()

        res = 0
        for num in cost:
            if num == 0: continue
            res += cost[num]
        return res