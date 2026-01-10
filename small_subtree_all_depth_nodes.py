# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxDepths = {}
        def dfs(node, depth):
            if not node:
                return 0
            res = depth
            res = max(dfs(node.left, depth+1), res)
            res = max(dfs(node.right, depth+1), res)
            maxDepths[id(node)] = res
            return res
        
        dfs(root, 1)
        maxD = max(maxDepths.values())

        def getDepth(node):
            if not node:
                return 0
            return maxDepths[id(node)]


        def rec(node):
            if not node.left and not node.right:
                return node
            if not node.left:
                return rec(node.right)
            if not node.right:
                return rec(node.left)
            if maxDepths[id(node.left)] == maxDepths[id(node.right)]:
                return node
            if maxDepths[id(node.left)] > maxDepths[id(node.right)]:
                return rec(node.left)
            else:
                return rec(node.right)
        return rec(root)
            
            