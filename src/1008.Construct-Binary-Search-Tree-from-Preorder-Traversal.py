# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        pivot = preorder[0]
        root = TreeNode(pivot)
        idx = -1
        for i in range(1, len(preorder)):
            if preorder[i] > pivot:
                idx = i
                break
        if idx == -1:
            root.left = self.bstFromPreorder(preorder[1:])
            root.right = None
        else:
            root.left = self.bstFromPreorder(preorder[1:idx])
            root.right = self.bstFromPreorder(preorder[idx:])
        return root