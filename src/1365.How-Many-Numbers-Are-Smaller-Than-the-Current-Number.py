class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        sorted_nums = sorted(nums)
        for i in range(n):
            ans[i] = bisect.bisect_left(sorted_nums, nums[i])
        
        return ans
