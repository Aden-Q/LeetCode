# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        
        @cache
        def dp(n) -> List[Optional[TreeNode]]:
            if n == 1:
                return [TreeNode()]

            res = []
            for left_num_nodes in range(1, n, 2):
                right_num_nodes = n - 1 - left_num_nodes
                left_subtrees = dp(left_num_nodes)
                right_subtrees = dp(right_num_nodes)
                for left_subtree in left_subtrees:
                    for right_subtree in right_subtrees:
                        res.append(TreeNode(0, left_subtree, right_subtree))

            return res

        return dp(n)
