class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        n = len(s)
        addCount = int(10/gcd(10, a))
        cycleCount = int(n / gcd(n, b))
        digits = "0123456789"
        
        
        def getMin(oddAdds, evenAdds):
            sNew = list(s)
            
            for i in range(1, n, 2):
                sNew[i] = digits[(ord(s[i]) - ord('0') + oddAdds * a)%10]
            
            for i in range(0, n, 2):
                sNew[i] = digits[(ord(s[i]) - ord('0') + evenAdds * a)%10]
            res = "".join(sNew)

            for i in range(cycleCount):
                sNewNew = list(s)
                for j in range(n):
                    sNewNew[j] = sNew[(j + b) % n]
                sNew = sNewNew
                res = min(res, "".join(sNew))
            return res
        res = s
        if b % 2:
            for i in range(addCount):
                for j in range(addCount):
                    res = min(res, getMin(i,j))

        else:
            for i in range(addCount):
                res = min(res, getMin(i, 0))
        return res
