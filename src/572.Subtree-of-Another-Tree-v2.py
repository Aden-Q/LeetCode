# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root or not subRoot:
            return root == subRoot
        
        def isSameTree(tree1, tree2):
            if not tree1 or not tree2:
                return tree1 == tree2
            if tree1.val != tree2.val:
                return False
            return isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right)
        
        return isSameTree(root, subRoot) or isSameTree(root.left, subRoot) or isSameTree(root.right, subRoot)