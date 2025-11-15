class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0


        prefixSum = [0] * n
        prefixSum[0] = 1 if s[0] == '1' else 0
        for i in range(1, n):
            prefixSum[i] = prefixSum[i-1]
            if s[i] == '1':
                prefixSum[i] += 1

        onesRight = [0] * n
        nextZero = [n] * n
        zeroIndex = n
        for i in range(n-1, -1, -1):
            nextZero[i] = zeroIndex
            if s[i] == '0':
                zeroIndex = i

        ones = 0
        for i in range(n-1, -1, -1):
            onesRight[i] = ones
            if s[i] == '0':
                ones = 0
            else:
                ones += 1
        
        for l in range(n):
            curr = l
            for j in range(int(math.sqrt(n)) + 1):
                ones = prefixSum[curr] - (prefixSum[l-1] if l > 0 else 0)
                zeros = curr - l + 1 - ones
                needed = zeros*zeros - ones
                if needed <= 0:
                    res += onesRight[curr] + 1
                else:
                    res += max(0, onesRight[curr] + 1 - needed)

                curr = nextZero[curr]
                if curr == n:
                    break
                

        return res

