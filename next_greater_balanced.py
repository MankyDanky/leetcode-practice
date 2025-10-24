class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        count = [0]*10
        num = n

        def balanced():
            nonlocal count
            if count[0] != 0:
                return False
            
            for i in range(1, 10):
                if count[i] != 0 and count[i] != i:
                    return False
            return True
        
        while (num != 0):
            count[(num%10)] += 1
            num //= 10
        
        while True:
            n += 1
            num = n
            while num%10 == 0:
                count[9] -= 1
                count[0] += 1
                num //= 10
            if num%10 == 1 and (num//10) == 0:
                count[1] += 1
            else:
                count[(num%10)-1] -= 1
                count[num%10] += 1

            if balanced():
                return n