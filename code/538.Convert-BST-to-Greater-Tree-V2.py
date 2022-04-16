# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # 右中左递归
        self.convertBST(root.right)
        self.sum += root.val
        root.val = self.sum
        self.convertBST(root.left)
        return root