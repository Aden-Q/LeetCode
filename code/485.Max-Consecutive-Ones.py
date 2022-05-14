class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        start = 0
        count = 0
        max_count = 0
        right = start
        while start < len(nums) and right < len(nums):
            if nums[start] != 1:
                start += 1
                right = start
                count = 0
                continue
            if nums[right] == 1:
                count += 1
                right += 1
                max_count = max(max_count, count)
            else:
                start = right
        return max_count