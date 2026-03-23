class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)

        def rotate(mat):
            newMat = []
            for j in range(n):
                curr = []
                for i in range(n):
                    curr.append(mat[i][j])
                curr.reverse()
                newMat.append(curr)
            return newMat
        
        for i in range(4):
            mat = rotate(mat)
            if mat == target:
                return True
        return False