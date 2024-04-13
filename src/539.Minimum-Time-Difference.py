# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        def traverse(root):
            if not root:
                return 0
            left_height = traverse(root.left)
            right_height = traverse(root.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return max(left_height, right_height) + 1
        
        traverse(root)
        return self.diameter