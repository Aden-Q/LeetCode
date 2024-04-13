# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0
    val = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return 0
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            self.val = root.val
        self.kthSmallest(root.right, k)
        return self.val