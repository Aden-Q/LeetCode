class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(nums, target, start, end):
            if start > end:
                return -1
            idx = (start + end) // 2
            if nums[idx] == target:
                return idx
            elif nums[idx] > target:
                return binary_search(nums, target, start, idx-1)
            else:
                return binary_search(nums, target, idx+1, end)
        
        return binary_search(nums, target, 0, len(nums)-1)