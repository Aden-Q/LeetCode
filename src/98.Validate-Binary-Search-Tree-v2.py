# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # the sequence of a valid BST must be increasing
        traverse = []

        def dfs(node) -> bool:
            nonlocal traverse
            if not node:
                return True
            if not dfs(node.left):
                return False
            traverse.append(node.val)
            if len(traverse) > 1 and traverse[-1] <= traverse[-2]:
                return False
            if not dfs(node.right):
                return False
            
            return True

        return dfs(root)
