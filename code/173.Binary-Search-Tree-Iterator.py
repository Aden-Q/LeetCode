# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.ptr = -1
        self.inorder = []
        self.traverse(root)
        
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        self.inorder.append(root.val)
        self.traverse(root.right)
        
    def next(self) -> int:
        if (self.ptr + 1) < len(self.inorder):
            self.ptr += 1
        return self.inorder[self.ptr]

    def hasNext(self) -> bool:
        if (self.ptr + 1) < len(self.inorder):
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()