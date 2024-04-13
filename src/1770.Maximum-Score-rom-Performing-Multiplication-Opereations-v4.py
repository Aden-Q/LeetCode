class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n, m = len(nums), len(multipliers)

        # a 2d dp array
        prev_row = [0] * (m+1)
        curr_row = [0] * (m+1)

        for left in reversed(range(n)):
            for idx in reversed(range(left, m)):
                curr_row[idx] = max(nums[left] * multipliers[idx] + prev_row[idx+1], nums[n-1-(idx-left)] * multipliers[idx] + curr_row[idx+1])
            curr_row, prev_row = prev_row, curr_row

        return prev_row[0]