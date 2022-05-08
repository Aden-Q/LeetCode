# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def buildTree(low, high):
            res = []
            if low > high:
                res.append(None)
                return res
            for i in range(low, high+1):
                left_trees = buildTree(low, i-1)
                right_trees = buildTree(i+1, high)
                for lt in left_trees:
                    for rt in right_trees:
                        root = TreeNode(i)
                        root.left = lt
                        root.right = rt
                        res.append(root)
            return res
        
        return buildTree(1, n)