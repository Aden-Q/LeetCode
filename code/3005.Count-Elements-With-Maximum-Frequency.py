class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter_nums = Counter(nums)
        total_freq = 0
        max_freq = max(counter_nums.values())
        for val in counter_nums.values():
            if val == max_freq:
                total_freq += max_freq

        return total_freq
