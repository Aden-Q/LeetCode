from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []
        for key, val in counter.items():
            if val == 1:
                res.append(key)
                if len(res) == 2:
                    return res