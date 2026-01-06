# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 1
        q = deque([root])
        s = float("-inf")
        x = 1
        res = 1
        while q:
            t = len(q)
            c = 0
            for i in range(t):
                node = q.popleft()
                c += node.val
                if node.left != None:
                    q.append(node.left)
                if node.right != None:
                    q.append(node.right)
            if c > s:
                res = x
                s = c
            x += 1
        return res