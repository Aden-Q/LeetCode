# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        path = [root.val]
        
        def dfs(root, curSum):
            if not root.left and not root.right and curSum == targetSum:
                res.append(path[:])
                
            if root.left:
                path.append(root.left.val)
                dfs(root.left, curSum + root.left.val)
                path.pop()
            if root.right:
                path.append(root.right.val)
                dfs(root.right, curSum + root.right.val)
                path.pop()
            
            return
        
        dfs(root, root.val)
        return res