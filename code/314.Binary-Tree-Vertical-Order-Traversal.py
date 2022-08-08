# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = [[] for _ in range(202)]
        left_ptr, right_ptr = 101, 101
        
        def traverse(root, cur_ptr, depth):
            nonlocal res, left_ptr, right_ptr
            if not root:
                return
            # update boundary
            left_ptr = min(left_ptr, cur_ptr)
            right_ptr = max(right_ptr, cur_ptr)
            res[cur_ptr].append((depth, root.val))
            traverse(root.left, cur_ptr - 1, depth + 1)
            traverse(root.right, cur_ptr + 1, depth + 1)
            return
            
        traverse(root, 101, 0)
        vet = []
        for c in res[left_ptr:right_ptr+1]:
            c.sort(key = lambda a : a[0])
            vet.append([x[1] for x in c])
        
        return vet