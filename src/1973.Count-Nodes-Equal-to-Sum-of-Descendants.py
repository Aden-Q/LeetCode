# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def equalToDescendants(self, root: Optional[TreeNode]) -> int:
        # dfs post order traversal
        # for every node we visited, return the sum of all its descendants + its own value
        cnt = 0

        def dfs(node) -> int:
            nonlocal cnt
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            if left_sum + right_sum == node.val:
                cnt += 1

            return left_sum + right_sum + node.val

        dfs(root)
        return cnt
