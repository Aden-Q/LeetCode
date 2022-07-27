# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorder_list = []
        def traverse(root):
            if not root:
                return
            preorder_list.append(root)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        for i in range(len(preorder_list) - 1):
            preorder_list[i].left = None
            preorder_list[i].right = preorder_list[i+1]