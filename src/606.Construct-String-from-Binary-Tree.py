# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        path = []
        
        def traverse(root):
            nonlocal path
            if not root:
                path.append('')
                return
            path.append('%d' % root.val)
            if root.left:
                path.append('(')
                traverse(root.left)
                path.append(')')
                if root.right:
                    path.append('(')
                    traverse(root.right)
                    path.append(')')
            else:
                if root.right:
                    path.append('(')
                    path.append(')')
                    path.append('(')
                    traverse(root.right)
                    path.append(')')
            
        traverse(root)
        return ''.join(path)