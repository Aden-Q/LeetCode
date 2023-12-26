# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        # run dfs to collect nodes from left to right
        def collectLeaves(root) -> List[int]:
            if not root:
                return []
            
            if not root.left and not root.right:
                return [root.val]
            
            return collectLeaves(root.left) + collectLeaves(root.right)
        
        l1 = collectLeaves(root1)
        l2 = collectLeaves(root2)

        return l1 == l2
