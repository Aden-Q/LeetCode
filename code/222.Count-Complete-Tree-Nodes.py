# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0

        if not root:
            return count
        
        q = deque([root])
        while q:
            size = len(q)
            count += size
            for _ in range(size):
                node = q.popleft()
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
                    
        return count