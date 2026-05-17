class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        output = ""
        for i in range(len(nums)):
            if nums[i][i] == "0":
                output += "1"
            else:
                output += "0"
        return output