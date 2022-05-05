# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memory = {}
        res = []
        
        def traverse(root):
            nonlocal res
            if not root:
                return '#'
            left = traverse(root.left)
            right = traverse(root.right)
            subtree_str = left + ',' + right + ',' + str(root.val)
            if subtree_str in memory:
                if memory[subtree_str] == 1:
                    res.append(root)
                memory[subtree_str] += 1
            else:
                memory[subtree_str] = 1
            return subtree_str
        
        traverse(root)
        return res