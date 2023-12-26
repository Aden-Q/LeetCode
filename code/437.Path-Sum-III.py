# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # we can run dfs and keep the cumulative path sum in a hashset
        # when we reach a node and get a new sum 'curr_sum', we simply need
        # to check whether curr_sum - targetSum is in the dict or not
        # to account for duplicates, we need to maintain a hashtable (counter)
        # instead of a hashset
        if not root:
            return 0

        counter = Counter({0: 1})
        cnt = 0

        def dfs(node, counter, curr_sum):
            nonlocal cnt

            if not node:
                return
            curr_sum = curr_sum + node.val
            cnt += counter[curr_sum - targetSum]
            counter[curr_sum] += 1

            dfs(node.left, counter, curr_sum)
            dfs(node.right, counter, curr_sum)

            counter[curr_sum] -= 1
            return

        dfs(root, counter, 0)
        return cnt