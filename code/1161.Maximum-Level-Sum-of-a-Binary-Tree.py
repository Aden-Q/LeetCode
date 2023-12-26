# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        max_level_idx = 0
        max_level_sum = -math.inf

        level_idx = 0
        queue = deque([root])
        while queue:
            size = len(queue)
            level_sum = 0
            level_idx += 1

            for _ in range(size):
                curr = queue.popleft()
                level_sum += curr.val
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
            
            if level_sum > max_level_sum:
                max_level_idx = level_idx
                max_level_sum = level_sum
        
        return max_level_idx
