# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = []
        def inorderTraversal(root):
            if not root:
                return
            inorderTraversal(root.left)
            result.append(root.val)
            inorderTraversal(root.right)
            
        inorderTraversal(root)
        for i in range(len(result) - 1):
            if result[i+1] <= result[i]:
                return False
        
        return True