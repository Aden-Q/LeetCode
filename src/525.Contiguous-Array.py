class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        d = {}
        d[0] = -1
        cur_sum = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cur_sum -= 1
            else:
                cur_sum += 1
            if cur_sum in d:
                res = max(res, i - d[cur_sum])
            else:
                d[cur_sum] = i
        return res