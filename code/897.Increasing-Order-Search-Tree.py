# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        inorder = []
        if not root:
            return root
        def traverse(root):
            nonlocal inorder
            if not root:
                return
            traverse(root.left)
            inorder.append(root)
            traverse(root.right)
            return
        traverse(root)
        root = inorder[0]
        cur = root
        for i in range(1, len(inorder)):
            cur.left = None
            cur.right = inorder[i]
            cur = cur.right
        cur.left = None
        cur.right = None
        return root