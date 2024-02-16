# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        min_dist = float('inf')
        ans = root.val
        node = root
        while node:
            dist = abs(node.val - target)
            if dist < min_dist:
                ans = node.val
                min_dist = abs(node.val - target)
            elif dist == min_dist:
                ans = min(ans, node.val)
            if node.val < target:
                node = node.right
            elif node.val > target:
                node = node.left
            else:
                break

        return ans
