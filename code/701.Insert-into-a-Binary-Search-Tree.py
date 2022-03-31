# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        cur = root
        if not root:
            return TreeNode(val)
        while cur:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    break
                else:
                    cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    break
                else:
                    cur = cur.left
        return root