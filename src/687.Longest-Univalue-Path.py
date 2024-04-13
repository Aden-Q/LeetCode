# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        longest_path = 0
        
        # longestPath(node) counts the number of nodes whose value is equal to node's value starting from node 
        @lru_cache
        def longestPath(node, val) -> int:
            nonlocal longest_path
            if not node:
                return 0

            left_count = longestPath(node.left, node.val)
            right_count = longestPath(node.right, node.val)

            longest_path = max(longest_path, left_count + right_count)
            
            return 0 if node.val != val else max(left_count, right_count) + 1

        longestPath(root, root.val)

        return longest_path
