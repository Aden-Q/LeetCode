# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0

        # run preorder traversal
        def dfs(node):
            if not node:
                return

            # if the curernt node's value is odd
            # recursively check its children
            if node.val & 1:
                dfs(node.left)
                dfs(node.right)
                return

            # find the current node's grandchildren
            left_sum = 0
            if node.left:
                if node.left.left:
                    left_sum += node.left.left.val
                if node.left.right:
                    left_sum += node.left.right.val

            right_sum = 0
            if node.right:
                if node.right.left:
                    right_sum += node.right.left.val
                if node.right.right:
                    right_sum += node.right.right.val
            
            self.ans += left_sum + right_sum
            # here is the trick to trim the tree, when nothing to explore in the subtree
            if left_sum:
                dfs(node.left)
            if right_sum:
                dfs(node.right)

        dfs(root)
        return self.ans