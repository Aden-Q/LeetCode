class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # simply sliding window
        maxLen = 0
        left = right = 0
        window = Counter()
        while right < len(nums):
            window[nums[right]] += 1
            while window[nums[right]] > k:
                window[nums[left]] -= 1
                left += 1
            
            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen
