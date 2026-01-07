# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        MOD = 1000000007

        res = 0
        cache = {}
        def sm(node):
            if not node:
                return 0
            if id(node) in cache:
                return cache[id(node)]
            res = node.val + sm(node.left) + sm(node.right)
            cache[id(node)] = res
            return res
        
        def rec(node, s):
            if not node:
                return 0
            res = 0
            if node.left:
                res = sm(node.left) * (s + node.val + sm(node.right))
            if node.right:
                res = max(res, sm(node.right) * (s + node.val + sm(node.left)))
            res = max(res, max(rec(node.left, s + node.val + sm(node.right)), rec(node.right, s + node.val + sm(node.left))))
            return res
        return rec(root, 0) % MOD