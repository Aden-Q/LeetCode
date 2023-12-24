class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, 0
        curr_sum = 0
        max_sum = -math.inf

        while right < len(nums):
            curr_sum += nums[right]
            while right - left + 1 > k:
                curr_sum -= nums[left]
                left += 1
            
            if right - left + 1 == k:
                max_sum = max(max_sum, curr_sum)
            
            right += 1

        return max_sum / k