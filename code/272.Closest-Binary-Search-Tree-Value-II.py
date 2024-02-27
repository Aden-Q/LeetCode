# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        max_heap = []

        # inorder traversal
        # the return value is used for early return
        def traverse(node) -> bool:
            nonlocal max_heap
            if not node:
                return False

            if traverse(node.left):
                return True

            if len(max_heap) < k:
                heapq.heappush(max_heap, (-abs(node.val - target), node.val))
            elif -max_heap[0][0] < abs(node.val - target):
                return True
            else:
                heapq.heappushpop(max_heap, (-abs(node.val - target), node.val))

            if traverse(node.right):
                return True

        traverse(root)
        return [key[1] for key in max_heap]
