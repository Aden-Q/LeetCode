class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        n = len(nums)

        def generateSubseqences(nums):
            ans = set([0])
            for num in nums:
                ans.update([num + val for val in ans])

            return ans

        sub_vals = sorted(generateSubseqences(nums[1::2]))
        ans = inf
        for val in generateSubseqences(nums[::2]):
            idx = bisect_left(sub_vals, goal-val)
            if idx < len(sub_vals):
                ans = min(ans, abs(sub_vals[idx] + val - goal))
            if idx > 0:
                ans = min(ans, abs(sub_vals[idx-1] + val - goal))
        
        return ans
