class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        nums.sort()
        for end in range(2, len(nums)):
            left, right = 0, end - 1
            while left < right:
                if nums[left] + nums[right] > nums[end]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res