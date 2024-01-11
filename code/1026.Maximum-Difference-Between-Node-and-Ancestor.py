# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        v = 0

        def traverse(node, min_val, max_val):
            nonlocal v
            if not node:
                return

            v = max(v, abs(node.val - min_val), abs(node.val - max_val))

            traverse(node.left, min(min_val, node.val), max(max_val, node.val))
            traverse(node.right, min(min_val, node.val), max(max_val, node.val))

            return
        
        traverse(root, root.val, root.val)
        return v