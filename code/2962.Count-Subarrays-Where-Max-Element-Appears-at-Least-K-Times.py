class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxElement = max(nums)
        n = len(nums)
        left = right = 0
        window = Counter()
        less_than_k_cnt = 0
        total = n * (n-1) // 2 + n
        while right < n:
            window[nums[right]] += 1

            while window[maxElement] >= k:
                window[nums[left]] -= 1
                left += 1
            
            less_than_k_cnt += right - left + 1

            right += 1
        
        return total - less_than_k_cnt
