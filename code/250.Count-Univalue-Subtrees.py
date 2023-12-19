# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        # a global counter to count the number of uni-value subtrees
        cnt = 0

        # dfs return true if the subtree rooted at node is a uni-value subtree
        # a subtree is a uni-value subtree if and only if its left and right subtrees
        # are both uni-value subtrees and they have the same value as the root node's value 
        def dfs(node) -> bool:
            nonlocal cnt
            if not node:
                return True
            
            left = dfs(node.left)
            right = dfs(node.right)
            # if either the left subtree or right subtree is not a uni-value subtree
            # the subtree rooted at node is not a uni-value subtree
            if not left or not right:
                return False
            if node.left and node.left.val != node.val:
                return False
            if node.right and node.right.val != node.val:
                return False
            # passed tests, the subtree rooted at node is a uni-value subtree
            cnt += 1
            return True
        
        dfs(root)
        return cnt
