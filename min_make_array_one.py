import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        
        n = len(nums)
        if 1 in nums:
            return n - nums.count(1)

        res = float("inf")

        for i in range(n):
            distance = 100
            # Make 1 from left
            for j in range(i-1, -1, -1):
                arr = list(nums)
                for k in range(j, i):
                    g = math.gcd(arr[k+1], arr[k])
                    if (arr[k+1] != g):
                        arr[k+1] = g
                    else:
                        break
                if arr[i] == 1:
                    distance = i - j
                    break
            
            for j in range(i+1, n):
                arr = list(nums)
                for k in range(i+1, j+1):
                    g = math.gcd(arr[k-1], arr[k])
                    if (arr[k-1] != g):
                        arr[k-1] = g
                    else:
                        break
                if arr[i] == 1:
                    distance = min(distance, j - i)
                    break
            if distance == 100:
                continue
            # Make others 1
            res = min(res, distance + n - 1)
        return res if res != float("inf") else -1
                    
                    

                    

            
            # Make 1 from right


        

