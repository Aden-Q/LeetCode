"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        # if the current node has a right child, then its inorder successor must be in its right subtree
        # moreover, its inorder successor is the leftmost node of its right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node

        # if the current node does not have a right child, then its successor must be on its parent path
        # we need to find the first parent link goes left (the minimum value which is larger than node's value)
        while node.parent:
            if node == node.parent.left:
                return node.parent
            node = node.parent

        # if we cannot find a left link, this means that the current node does not have a successor
        return None
