"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        depth = 0
        if not root:
            return depth
        
        q = deque([root])
        while q:
            size = len(q)
            depth += 1
            for _ in range(size):
                node = q.popleft()
                for child in node.children:
                    if node:    q.append(child)
                    
        return depth