# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
        q = deque([root])
        while q:
            size = len(q)
            cur_largest = float('-inf')
            for _ in range(size):
                node = q.popleft()
                if node.val > cur_largest:
                    cur_largest = node.val
                if node.left:   q.append(node.left)
                if node.right:  q.append(node.right)
            res.append(cur_largest)
        
        return res