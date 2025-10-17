class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        if k == 26:
            return 1

        n = len(s)
        
        left = [[0] * 3 for _ in range(n)]
        right = [[0] * 3 for _ in range(n)]


        count, mask, num = 0, 0, 0
        for i in range(n-1):
            bit = 1<<(ord(s[i]) - ord('a'))
            if not (mask & bit):
                count += 1
                if count <= k:
                    mask |= bit
                else:
                    count = 1
                    mask = bit
                    num += 1
            left[i+1][0] = num
            left[i+1][1] = mask
            left[i+1][2] = count

        count, mask, num = 0, 0, 0
        for i in range(n-1, 0, -1):
            bit = 1<<(ord(s[i]) - ord('a'))
            if not (mask & bit):
                count += 1
                if count <= k:
                    mask |= bit
                else:
                    count = 1
                    mask = bit
                    num += 1
            right[i-1][0] = num
            right[i-1][1] = mask
            right[i-1][2] = count
        
        res = 0
        for i in range(n):
            temp = left[i][0] + right[i][0] + 2
            total_mask = left[i][1] | right[i][1]
            if min(total_mask.bit_count() + 1, 26) <= k:
                temp -= 1
            elif left[i][2] == k and right[i][2] == k and total_mask.bit_count() < 26:
                temp += 1
            res = max(res, temp)
        return res
            

