# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        max_size = 0

        # for the subtree rootat at node, returns (whether it is a BST, size, min value, max value)
        def traverse(node) -> (bool, int, int, int):
            nonlocal max_size
            if not node:
                return True, 0, float('inf'), -float('inf')

            left_is_BST, left_size, left_min, left_max = traverse(node.left)
            right_is_BST, right_size, right_min, right_max = traverse(node.right)

            is_BST = left_is_BST and right_is_BST and left_max < node.val < right_min
            size = left_size + right_size + 1
            min_val = min(left_min, right_min, node.val)
            max_val = max(left_max, right_max, node.val)

            if is_BST:
                max_size = max(max_size, size)

            return is_BST, size, min_val, max_val

        traverse(root)
        return max_size
