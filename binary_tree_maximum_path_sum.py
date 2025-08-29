# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    cached_max_sums = {}

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return float("-inf")
        return max(root.val + self.sum_path(root.left) + self.sum_path(root.right), self.maxPathSum(root.left), self.maxPathSum(root.right), root.val)

    def sum_path(self, node):
        if not node:
            return 0
        if node in self.cached_max_sums:
            return self.cached_max_sums[node]
        s = max(node.val, node.val + self.sum_path(node.left), node.val + self.sum_path(node.right), 0)
        self.cached_max_sums[node] = s
        return s
        
