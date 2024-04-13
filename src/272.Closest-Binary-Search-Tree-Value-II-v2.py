# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        inorder_sequence = []

        def traverse(node):
            nonlocal inorder_sequence
            if not node:
                return

            traverse(node.left)
            inorder_sequence.append(node.val)
            traverse(node.right)

            return

        traverse(root)
        res = []

        # binary search
        idx = bisect.bisect_left(inorder_sequence, target)
        
        left, right = idx-1, idx
        while k:
            if right >= len(inorder_sequence):
                res.extend(inorder_sequence[left+1-k:left+1])
                break
            elif left < 0:
                res.extend(inorder_sequence[right:right+k])
                break
            elif abs(target - inorder_sequence[left]) < abs(target - inorder_sequence[right]):
                res.append(inorder_sequence[left])
                left -= 1
            else:
                res.append(inorder_sequence[right])
                right += 1
            
            k -= 1

        return res
