class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_num = max(nums)
        # max_points[k] represents the maximum number of points we can obtain if we use all numbers <= k
        state1, state2 = 0, counter[1]

        for i in range(2, max_num+1):
            state1, state2 = state2, max(state2, state1 + i * counter[i])

        return state2
