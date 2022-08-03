# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.res = [[] for _ in range(100)]
        self.max_height = 0
        
        def traverse(root):
            if not root:
                return -1
            cur_height = max(traverse(root.left), traverse(root.right)) + 1
            self.max_height = max(self.max_height, cur_height)
            self.res[cur_height].append(root.val)
            return cur_height
        
        traverse(root)
        return self.res[:self.max_height + 1]