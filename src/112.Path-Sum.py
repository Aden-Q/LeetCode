# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        def backtracking(node, path_sum):
            if not node.left and not node.right:
                if path_sum == targetSum:
                    return True
                else:
                    return False
            
            if node.left:
                if backtracking(node.left, path_sum + node.left.val):    return True
            if node.right:
                if backtracking(node.right, path_sum + node.right.val):   return True
            
            return False
        
        return backtracking(root, root.val)