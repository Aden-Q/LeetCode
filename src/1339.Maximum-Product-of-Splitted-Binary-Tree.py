# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        total_sum = 0
        # we don't care about duplicate sums
        subtree_sums = set()

        # post order traversal, process the sum on the way
        # this function returns the sum of the subtree rooted at the given node
        def dfs(node) -> int:
            nonlocal total_sum, subtree_sums
            if not node:
                return 0

            total_sum += node.val
            left_subtree_sum = dfs(node.left)
            right_subtree_sum = dfs(node.right)
            subtree_sum = node.val + left_subtree_sum + right_subtree_sum
            subtree_sums.add(subtree_sum)

            return subtree_sum

        dfs(root)

        max_prod = 0
        for subtree_sum in subtree_sums:
            max_prod = max(max_prod, (total_sum - subtree_sum) * subtree_sum)

        return max_prod % (10 ** 9 + 7)
