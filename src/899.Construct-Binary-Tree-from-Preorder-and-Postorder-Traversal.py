# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        def traverse(root, preorder, postorder):
            if len(preorder) == 0:
                return None
            if len(preorder) == 1:
                return TreeNode(preorder[0])
            pivot = preorder[1]
            idx = postorder.index(pivot)
            root = TreeNode(preorder[0])
            root.left = traverse(root.left, preorder[1:idx+2], postorder[:idx+1])
            root.right = traverse(root.right, preorder[idx+2:], postorder[idx+1:-1])
            return root
        return traverse(TreeNode(), preorder, postorder)