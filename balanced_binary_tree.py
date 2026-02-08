# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        @lru_cache
        def get_depth(node):
            if not node:
                return 0
            return 1 + max(get_depth(node.left), get_depth(node.right))
        
        def balanced(node):
            if not node:
                return True
            
            return abs(get_depth(node.left) - get_depth(node.right)) <= 1 and balanced(node.left) and balanced(node.right)
        
        return balanced(root)
