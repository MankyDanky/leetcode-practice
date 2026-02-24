# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        nums = []

        def rec(node, curr):
            if not node:
                return
            curr<<=1
            curr += node.val
            if not node.left and not node.right:
                nums.append(curr)
                return
            rec(node.left, curr)
            rec(node.right, curr)
        
        rec(root, 0)
        return sum(nums)