# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        # postorder traversal
        # returns the max sum of the path starting from the current node to a leaf of the subtree
        # pre_sum is the path sum from root to the current node
        def dfs(node, pre_sum) -> int:
            if not node:
                return 0

            max_path_sum = -float('inf')

            # now we need to check if we need to delete its children
            if node.left:
                max_path_sum_left = dfs(node.left, pre_sum + node.left.val)
                if max_path_sum_left + pre_sum < limit:
                    node.left = None

                max_path_sum = max(max_path_sum, max_path_sum_left + node.val)
                
            if node.right:
                max_path_sum_right = dfs(node.right, pre_sum + node.right.val)
                if max_path_sum_right + pre_sum < limit:
                    node.right = None

                max_path_sum = max(max_path_sum, max_path_sum_right + node.val)

            return max_path_sum if max_path_sum != -float('inf') else node.val

        dummy = TreeNode(0, root)
        dfs(dummy, 0)

        return dummy.left
