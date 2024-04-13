from collections import Counter

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = Counter(range(1, len(nums) + 1))
        for num in nums:
            del res[num]
        return list(res.keys())