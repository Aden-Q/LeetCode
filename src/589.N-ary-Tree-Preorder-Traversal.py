"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        
        def traverse(node):
            nonlocal res
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                traverse(child)
            return
        
        traverse(root)
        return res
            