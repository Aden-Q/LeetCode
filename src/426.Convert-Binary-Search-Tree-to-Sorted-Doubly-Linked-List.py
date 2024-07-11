"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return root

        inorder_list = []

        def traverse(node):
            nonlocal inorder_list
            if not node:
                return

            traverse(node.left)
            inorder_list.append(node)
            traverse(node.right)

        traverse(root)

        n = len(inorder_list)

        for i in range(n - 1):
            inorder_list[i].right = inorder_list[i + 1]
            inorder_list[i + 1].left = inorder_list[i]

        inorder_list[0].left = inorder_list[-1]
        inorder_list[-1].right = inorder_list[0]

        return inorder_list[0]
