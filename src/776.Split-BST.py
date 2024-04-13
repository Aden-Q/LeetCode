# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root:
            return [None, None]

        if target == root.val:
            right_subtree = root.right
            root.right = None
            return [root, right_subtree]
        if target < root.val:
            # recursively split the left subtree
            split_left, split_right = self.splitBST(root.left, target)
            root.left = split_right
            return [split_left, root]
        else:
            # recursively split the right subtree
            split_left, split_right = self.splitBST(root.right, target)
            root.right = split_left
            return [root, split_right]
