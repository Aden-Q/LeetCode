from collections import Counter

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        d = Counter(set(nums1))
        res = []
        for item in set(nums2):
            if d[item] == 1:
                res.append(item)
            d[item] += 1
        for item in set(nums3):
            if d[item] == 1:
                res.append(item)
                
        return res