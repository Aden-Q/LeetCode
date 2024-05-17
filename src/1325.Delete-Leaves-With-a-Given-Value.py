# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        dummy =TreeNode()
        dummy.left = root

        def traverse(node, parent) -> None:
            if not node:
                return
            
            traverse(node.left, node)
            traverse(node.right, node)

            if not node.left and not node.right and node.val == target:
                # delete this leaf node
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None

            return

        traverse(root, dummy)

        return dummy.left
