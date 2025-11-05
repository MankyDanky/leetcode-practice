class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        freq = defaultdict(int)
        top = SortedList()
        rest = SortedList()
        topSum = 0

        def Balance():
            nonlocal topSum
            while len(top) < x and rest:
                f, v = rest.pop()
                top.add((f, v))
                topSum += v * f
            while len(top) > x:
                f, v = top.pop(0)
                topSum -= v * f
                rest.add((f, v))
            while top and rest and rest[-1] > top[0]:
                f1, v1 = rest.pop()
                f2, v2 = top.pop(0)
                rest.add((f2, v2))
                top.add((f1, v1))
                topSum += f1 * v1 - f2 * v2
        
        def Add(num):
            nonlocal topSum
            prevFreq = freq[num]
            freq[num] += 1
            if (prevFreq, num) in top:
                top.remove((prevFreq, num))
                topSum -= prevFreq * num
            if (prevFreq, num) in rest:
                rest.remove((prevFreq, num))
            rest.add((freq[num], num))
            Balance()

        def Remove(num):
            nonlocal topSum
            prevFreq = freq[num]
            if (prevFreq, num) in top:
                top.remove((prevFreq, num))
                topSum -= prevFreq * num
            if (prevFreq, num) in rest:
                rest.remove((prevFreq, num))
            freq[num] -= 1
            if freq[num] > 0:
                rest.add((freq[num], num))
            Balance()
        res = []
        for i in range(k):
            Add(nums[i])
        res.append(topSum)

        for i in range(k, len(nums)):
            Remove(nums[i-k])
            Add(nums[i])
            res.append(topSum)
        return res
