# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        cnt = 0

        # post order dfs, returns the number of nodes in its subtree and the sum, rooted at node
        def dfs(node) -> (int, int):
            nonlocal cnt
            if not node:
                return 0, 0
            
            left_num_nodes, left_sum = dfs(node.left)
            right_num_nodes, right_sum = dfs(node.right)

            curr_num_nodes = left_num_nodes + right_num_nodes + 1
            curr_sum = left_sum + right_sum + node.val
            if curr_sum // curr_num_nodes == node.val:
                cnt += 1

            return curr_num_nodes, curr_sum

        dfs(root)
        return cnt
