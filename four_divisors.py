class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0
        primes = []
        sieve = [0] * (100001)
        for i in range(2, 100001):
            if sieve[i] == 0:
                primes.append(i)
                for j in range(i, 100001, i):
                    sieve[j] = i
        
        p = set(primes)
            
        res = 0
        for num in nums:
            c = 2
            s = 1 + num
            divs = []
            for d in range(2, int(math.sqrt(num)) + 1):
                if d in p and num % d == 0 and (num//d in p or num == d*d*d):
                    if (d * d == num):
                        c += 1
                        s += d
                        divs.append(d)
                        break
                    c += 2
                    s += d + int(num/d)
                    divs.append(d)
                    divs.append(num/d)

            if c == 4:
                print(num, divs)
                res += s
                    
        return res