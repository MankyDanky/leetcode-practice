class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        segs = []
        while i < n - 1:
            s = 0
            
            if nums[i+1] > nums[i]:
                s += nums[i]
                sPre = nums[i] + nums[i+1]
                j = i + 1
                while j < n and nums[j] > nums[j-1]:
                    s += nums[j]
                    sPre = max(s, sPre)
                    j += 1
                sPost = nums[j-1] + nums[j-2]
                t = nums[j-1]
                for k in range(j-2, i-1, -1):
                    t += nums[k]
                    sPost = max(sPost, t)
                segs.append((1, s, i, j-1, sPre, sPost))
                i = j - 1
            elif nums[i+1] < nums[i]:
                s += nums[i]
                j = i + 1
                while j < n and nums[j] < nums[j-1]:
                    s += nums[j]
                    j += 1
                segs.append((-1, s, i, j - 1))
                i = j - 1
            else:
                i += 1
        res = float("-inf")
        print(segs)
        for i in range(0, len(segs)-2):
            if segs[i][3] == segs[i+1][2] and segs[i+1][3] == segs[i+2][2] and segs[i][0] == 1 and segs[i+1][0] == -1 and segs[i+2][0] == 1:
                res = max(res, segs[i][5] + segs[i+1][1] + segs[i+2][4] - nums[segs[i+1][2]] - nums[segs[i+1][3]])    
        return res
            