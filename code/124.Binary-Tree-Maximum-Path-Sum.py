# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path_sum = -math.inf
        # calculate the maximum path sum starting from this node
        # either all the way down to its left subtree
        # or to its right subtree
        # or the node itself
        def maxNodeSum(node) -> int:
            if not node:
                return 0
            
            max_left_sum = maxNodeSum(node.left)
            max_right_sum = maxNodeSum(node.right)

            max_node_sum = max(max_left_sum, max_right_sum, 0) + node.val
            self.max_path_sum = max(self.max_path_sum, max_node_sum, max_left_sum + max_right_sum + node.val)

            return max_node_sum

        maxNodeSum(root)
        return self.max_path_sum