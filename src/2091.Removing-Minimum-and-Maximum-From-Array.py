class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        max_idx = min_idx = -1
        max_val = -inf
        min_val = inf
        for idx, num in enumerate(nums):
            if num > max_val:
                max_val = num
                max_idx = idx
            if num < min_val:
                min_val = num
                min_idx = idx

        return min(max(max_idx+1, min_idx+1), max(n - min_idx, n - max_idx), max_idx+1 + n - min_idx, min_idx+1 + n - max_idx)
