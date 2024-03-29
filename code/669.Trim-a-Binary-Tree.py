# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            # if key  not found
            return root
        if root.val == key:
            # key found
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # both left and right subtrees are not empty
                # find the minimum in its right subtree and delete it
                cur = root.right
                while cur.left:
                    cur = cur.left
                root.right = self.deleteNode(root.right, cur.val)
                root.val = cur.val
        elif root.val > key:
            # forwarding the deletion
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
        return root
    
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root:
            return root
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        if root.val > high or root.val < low:
            return self.deleteNode(root, root.val)
        if root.left:
            if root.left.val > high or root.left.val < low:
                root.left = self.deleteNode(root.left, root.left.val)
        if root.right:
            if root.right.val > high or root.right.val < low:
                root.right = self.deleteNode(root.right, root.right.val)
        return root