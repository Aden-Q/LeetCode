# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            node = q[-1]  # take the last node on the current level
            res.append(node.val)
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node.left:  q.append(node.left)
                if node.right:   q.append(node.right)
                
        return res