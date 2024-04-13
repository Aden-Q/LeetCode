# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_length = 1
        
        # traverse() return the maximum length of a consecutive sequence including root
        def traverse(root):
            nonlocal max_length
            if not root:
                return 0
            left_longest = traverse(root.left)
            right_longest = traverse(root.right)
            curr_longest = 1
            if left_longest > 0 and root.val == root.left.val - 1:
                curr_longest = left_longest + 1
            if right_longest > 0 and root.val == root.right.val - 1:
                curr_longest = max(curr_longest, right_longest + 1)
            max_length = max(max_length, curr_longest)
            return curr_longest
        
        traverse(root)
        return max_length