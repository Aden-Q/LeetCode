# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # returns the required sum for a tree rooted at node, given a parent value and a grandparent value
        def dfs(node, parent, gparent) -> int:
            if not node:
                return 0

            return dfs(node.left, node.val, parent) + dfs(node.right, node.val, parent) + (0 if gparent & 1 else node.val)

        return dfs(root, -1, -1)