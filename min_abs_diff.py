class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        res = []
        currMin = float("inf")
        for i in range(1, len(arr)):
            d = arr[i] - arr[i-1]
            if d < currMin:
                currMin = d
                res = []
            if arr[i] - arr[i-1] == currMin:
                res.append([arr[i-1], arr[i]])
        return res