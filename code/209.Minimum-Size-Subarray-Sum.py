class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        cur_sum = nums[0]
        size = len(nums)
        min_length = size + 1
        while left < size and right < size:
            if cur_sum < target:
                right += 1
                if right < size:
                    cur_sum += nums[right]
            else:
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                cur_sum -= nums[left]
                left += 1
                
        if min_length == size + 1:
            return 0
        else:
            return min_length    