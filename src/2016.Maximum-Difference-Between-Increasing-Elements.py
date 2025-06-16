class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        prefix_min = nums[0]
        n = len(nums)
        ans = -1

        for num in nums:
            if num > prefix_min:
                ans = max(ans, num - prefix_min)
            else:
                prefix_min = min(prefix_min, num)

        return ans
