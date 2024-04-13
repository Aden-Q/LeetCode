# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # level order traversal
        q = deque([root])
        cur_level_sum = 0
        while len(q) != 0:
            cur_level_sum = 0
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                cur_level_sum += cur.val
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            
        return cur_level_sum