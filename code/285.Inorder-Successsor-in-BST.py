# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        prev_visited = None
        target = None

        # inorder traversal with early termination
        def inorder(node) -> bool:
            nonlocal prev_visited, target
            if not node:
                return False

            if inorder(node.left):
                return True
            if prev_visited == p:
                target = node
                return True
            else:
                prev_visited = node
            if inorder(node.right):
                return True

            return False

        inorder(root)
        return target