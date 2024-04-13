# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(cloned, target):
            if not cloned:
                return cloned
            if cloned.val == target.val:
                return cloned
            ans_left = traverse(cloned.left, target)
            if ans_left != None:
                return ans_left
            else:
                return traverse(cloned.right, target)
        
        return traverse(cloned, target)