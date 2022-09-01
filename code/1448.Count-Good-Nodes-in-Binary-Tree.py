# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        cnt = 0
        
        def traverse(root, max_val):
            nonlocal cnt
            if not root:
                return
            if max_val <= root.val:
                cnt += 1
            max_val = max(max_val, root.val)
            
            traverse(root.left, max_val)
            traverse(root.right, max_val)
            return
        
        traverse(root, -10**4-1)
        return cnt