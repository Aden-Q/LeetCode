# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(inorder) == 0:
            return None
        def traverse(root, inorder, postorder):
            if len(inorder) == 0:
                return None
            pivot = postorder[-1]
            idx = inorder.index(pivot)
            root = TreeNode(pivot)
            root.left = traverse(root.left, inorder[:idx], postorder[:idx])
            root.right = traverse(root.right, inorder[idx+1:], postorder[idx:-1])
            return root
        return traverse(TreeNode(), inorder, postorder)