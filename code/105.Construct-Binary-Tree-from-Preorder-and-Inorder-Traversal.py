# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        def traverse(root, preorder, inorder):
            if len(preorder) == 0 or len(inorder) == 0:
                return None
            pivot = preorder[0]
            idx = inorder.index(pivot)
            root = TreeNode(pivot)
            root.left = traverse(root.left, preorder[1:idx+1], inorder[:idx])
            root.right = traverse(root.right, preorder[idx+1:], inorder[idx+1:])
            return root
        return traverse(TreeNode(), preorder, inorder)