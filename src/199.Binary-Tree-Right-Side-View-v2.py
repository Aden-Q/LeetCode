# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []

        def dfs(node, depth):
            if not node:
                return
            
            # if the current node is the first one on this level, then append to the final result
            if depth == len(self.res):
                self.res.append(node.val)
            
            # first go right
            dfs(node.right, depth+1)
            dfs(node.left, depth+1)

        dfs(root, 0)
        return self.res
