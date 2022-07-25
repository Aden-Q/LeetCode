class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect.bisect_left(nums, target)
        right = bisect.bisect_right(nums, target) - 1
        print(left, ' ', right)
        if left >= len(nums):
            left = -1
        elif nums[left] != target:
            left = -1
        if right > len(nums) - 1 or right < 0:
            right = -1
        elif nums[right] != target:
            right = -1
        
        return [left, right]