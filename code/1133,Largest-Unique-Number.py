class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        counter = Counter(nums)
        largest_num = -1
        for key, val in counter.items():
            if val > 1:
                continue
            largest_num = max(largest_num, key)

        return largest_num
