class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        m = len(mana)
        max_skill = max(skill)
        sum_skill = sum(skill)
        res = 0
        for i in range(n):
            res += skill[i] * mana[0]
        prev_start = 0

        def valid(j):
            time_prev = prev_start
            time = 0
            res = 0
            for i in range(n):
                time_prev += skill[i] * mana[j-1]
                res = max(res, time_prev - time)
                time += skill[i] * mana[j]
            return res
        
        for j in range(1, m):
            l = valid(j)
            overlap = prev_start + sum_skill * mana[j-1] - l
            res += sum_skill * mana[j] - overlap
        
            prev_start = l
        return res
