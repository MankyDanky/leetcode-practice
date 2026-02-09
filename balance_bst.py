# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def dfs(node):
            if not node: 
                return
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        values.sort()

        def create(l, r):
            if (l > r):
                return
            mid = (l+r) // 2
            v = values[mid]
            node = TreeNode(v)
            node.left = create(l, mid-1)
            node.right = create(mid+1, r)
            return node
        return create(0, len(values)-1)