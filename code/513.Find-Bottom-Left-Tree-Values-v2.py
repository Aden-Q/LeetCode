# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # level order traversal from right to left
        q = deque([root])
        val = root.val

        while q:
            node = q.popleft()
            val = node.val
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)

        return val
