class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        seq = []
        dp = []
        
        for num in obstacles:
            if not seq or num >= seq[-1]:
                seq.append(num)
                dp.append(len(seq))
            else:
                index = bisect.bisect_right(seq, num)
                dp.append(index + 1)
                seq[index] = num
        return dp