# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMax(self, nums):
        idx = -1
        max_val = -float('inf')
        for i in range(len(nums)):
            if nums[i] > max_val:
                max_val = nums[i]
                idx = i
        return idx, max_val
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        idx, max_val = self.findMax(nums)
        root = TreeNode(max_val)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[idx+1:])
        return root