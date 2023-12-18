# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # DFS with node's value contrained
        def dfs(node, low, high) -> bool:
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False

            if not dfs(node.left, low, node.val): return False
            if not dfs(node.right, node.val, high): return False
            return True

        return dfs(root, -math.inf, math.inf)
