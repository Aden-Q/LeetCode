# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        node_index = {}
        for idx, node in enumerate(inorder):
            node_index[node] = idx

        def dfs(pre_start, pre_end, in_start, in_end):
            # base case, when nothing to build
            if pre_end < pre_start:
                return None
            
            # build left subtree and right subtree recursively
            pivot = preorder[pre_start]
            index = node_index[pivot]
            left_in_start = in_start
            left_in_end = index - 1
            left_length = index - in_start
            right_in_start = index + 1
            right_in_end = in_end
            right_length = in_end - index

            left_pre_start = pre_start + 1
            left_pre_end = left_pre_start + left_length - 1
            right_pre_start = left_pre_end + 1
            right_pre_end = right_pre_start + right_length - 1
            
            curr = TreeNode(pivot)
            curr.left = dfs(left_pre_start, left_pre_end, left_in_start, left_in_end)
            curr.right = dfs(right_pre_start, right_pre_end, right_in_start, right_in_end)
            return curr

        return dfs(0, len(preorder) - 1, 0, len(inorder) - 1)
