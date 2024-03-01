class Solution:
    def findMin(self, nums: List[int]) -> int:
        # still binary search, but we need to search for the left boundary because of
        # possible duplicates
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (right - left) // 2 + left
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1

        return nums[left]
