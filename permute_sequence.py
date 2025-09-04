class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        k -= 1
        factorials = []
        curr = 1
        for i in range(n):
            factorials.append(curr)
            curr *= (i + 1)
        factorials = factorials[::-1]
        curr = k
        rep = []
        print(factorials)
        for i in range(n):
            rep.append(curr//factorials[i])
            curr -= (rep[i] * factorials[i])
        res = []
        popper = list(range(1, n+1))
        for i in range(n):
            res.append(str(popper.pop(rep[i])))
    
        return "".join(res)