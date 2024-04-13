# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        val_set = set()
        def traverse(node):
            nonlocal val_set
            if not node:
                return
            
            val_set.add(node.val)
            traverse(node.left)
            traverse(node.right)
            return

        traverse(root2)

        def loopUp(node) -> bool:
            nonlocal val_set
            if not node:
                return False
            if target - node.val in val_set:
                return True
            
            return loopUp(node.left) or loopUp(node.right)

        return loopUp(root1)
