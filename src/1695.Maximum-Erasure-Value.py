from collections import Counter
class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        ct = Counter()
        left = 0
        right = 0
        res = 0
        cur_sum = 0
        while right < len(nums) and left < len(nums):
            # print(left, ' ', right, ' ', cur_sum)
            cur = nums[right]
            right += 1
            ct[cur] += 1
            cur_sum += cur
            while ct[cur] > 1:
                ct[nums[left]] -= 1
                cur_sum -= nums[left]
                left += 1
            res = max(res, cur_sum)
        return res