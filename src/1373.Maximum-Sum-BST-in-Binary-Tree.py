# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        max_sum = 0
        # for a tree rooted at node, returns a tuple, the first is a boolean, indicating whether it's a BST
        # the second is an int, the sum of all nodes' values of the tree
        # the third is the lower bound of the tree (the smallest value)
        # the forth is the upper bound of the tree (the greatest value)
        def dfs(node) -> (bool, int, int, int):
            nonlocal max_sum
            if not node:
                return (True, 0, math.inf, -math.inf)

            left_is_BST, left_sum, left_lower, left_upper = dfs(node.left)
            right_is_BST, right_sum, right_lower, right_upper = dfs(node.right)

            curr_is_BST = False
            curr_sum = left_sum + right_sum + node.val
            curr_lower = min(node.val, left_lower, right_lower)
            curr_upper = max(node.val, left_upper, right_upper)
            if left_is_BST and right_is_BST and node.val > left_upper and node.val < right_lower:
                curr_is_BST = True
                max_sum = max(max_sum, curr_sum)

            return (curr_is_BST, curr_sum, curr_lower, curr_upper)

        dfs(root)
        return max_sum
