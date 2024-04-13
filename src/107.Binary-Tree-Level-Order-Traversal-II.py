# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
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
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            res.append(cur_level)
            
        return res[::-1]