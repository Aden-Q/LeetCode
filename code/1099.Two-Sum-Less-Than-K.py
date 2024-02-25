class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        max_sum = -1

        while left < right:
            curr_sum = nums[left] + nums[right]
            if curr_sum >= k:
                right -= 1
            else:
                left += 1
                max_sum = max(curr_sum, max_sum)

        return max_sum
