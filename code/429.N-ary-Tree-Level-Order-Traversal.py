"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        while q:
            size = len(q)
            cur_level = []
            for _ in range(size):
                node = q.popleft()
                cur_level.append(node.val)
                if node.children:
                    for child in node.children:
                        q.append(child)
            res.append(cur_level)
            
        return res