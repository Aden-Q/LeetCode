class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        state1 = nums[0]
        state2 = max(nums[0], nums[1])
        for i in range(2, n):
            state1, state2 = state2, max(nums[i] + state1, state2)
        return state2