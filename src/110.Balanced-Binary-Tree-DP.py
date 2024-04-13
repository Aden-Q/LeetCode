# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.heights = {}

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def getDepth(node) -> int:
            if not node:
                return 0

            if node in self.heights:
                return self.heights[node]
            
            height = 1 + max(getDepth(node.left), getDepth(node.right))
            self.heights[node] = height

            return height
        
        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)

        return abs(leftDepth - rightDepth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
