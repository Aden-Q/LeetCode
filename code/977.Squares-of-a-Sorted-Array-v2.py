from collections import deque

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = deque()
        left = 0
        right = len(nums) - 1
        while left <= right:
            square_left = nums[left] ** 2
            square_right = nums[right] ** 2
            if square_left > square_right:
                res.appendleft(square_left)
                left += 1
            else:
                res.appendleft(square_right)
                right -= 1
        return res    