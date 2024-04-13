# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            cur_level = []
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                cur_level.append(node.val)
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
        return cur_level[0]