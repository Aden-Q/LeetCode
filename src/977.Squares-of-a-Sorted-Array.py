class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            square_left = nums[left] ** 2
            square_right = nums[right] ** 2
            if square_left < square_right:
                res.insert(0, square_right)
                right -= 1
            else:
                res.insert(0, square_left)
                left += 1
        return res