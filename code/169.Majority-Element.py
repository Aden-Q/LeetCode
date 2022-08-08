from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ct = Counter(nums)
        for k, v in ct.items():
            if v > len(nums) // 2:
                return k