# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            new_root = TreeNode(val, root)
            return new_root

        def traverse(node, depth):
            if not node:
                return
            
            if depth == 0:
                old_left = node.left
                old_right = node.right
                node.left = TreeNode(val)
                node.left.left = old_left
                node.right = TreeNode(val)
                node.right.right = old_right
            else:
                traverse(node.left, depth-1)
                traverse(node.right, depth-1)
            
            return

        traverse(root, depth-2)
        return root
