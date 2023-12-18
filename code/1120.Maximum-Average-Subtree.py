# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        # a typical tail recursion problem
        max_average = 0

        # dfs(node) returns a tuple, the first element is the sum of all nodes' values rooted at node
        # the second element is the size of the subtree rooted at node
        def dfs(node) -> (float, int):
            nonlocal max_average

            if not node:
                return (0, 0)
            sum_left, num_left = dfs(node.left)
            sum_right, num_right = dfs(node.right)

            sum_cur = sum_left + sum_right + node.val
            num_cur = num_left + num_right + 1
            max_average = max(max_average, sum_cur / num_cur)

            return sum_cur, num_cur

        dfs(root)
        return max_average