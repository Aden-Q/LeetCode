# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        inorder_seq = []

        def traverse(node):
            nonlocal inorder_seq
            if not node:
                return

            traverse(node.left)
            inorder_seq.append(node.val)
            traverse(node.right)

            return

        traverse(root)
        n = len(queries)
        res = [[0, 0] for _ in range(n)]
        for i in range(n):
            idx = bisect.bisect_left(inorder_seq, queries[i])
            if idx == len(inorder_seq):
                res[i][0] = inorder_seq[-1]
                res[i][1] = -1
            elif inorder_seq[idx] == queries[i]:
                res[i][0] = queries[i]
                res[i][1] = queries[i]
            elif idx > 0:
                res[i][0] = inorder_seq[idx-1]
                res[i][1] = inorder_seq[idx]
            else:
                res[i][0] = -1
                res[i][1] = inorder_seq[idx]

        return res
