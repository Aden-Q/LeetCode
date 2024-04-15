# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        lonely_nodes = []

        def traverse(node, isOnlyChild) -> None:
            nonlocal lonely_nodes
            if not node:
                return

            if isOnlyChild:
                lonely_nodes.append(node.val)
            
            if node.left and node.right:
                traverse(node.left, False)
                traverse(node.right, False)
            else:
                traverse(node.left, True)
                traverse(node.right, True)

        traverse(root, False)
        return lonely_nodes
