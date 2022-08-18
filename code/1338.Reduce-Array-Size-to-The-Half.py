from collections import Counter
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        sz = len(arr)
        ct = Counter(arr)
        ct_list = [(k, v) for k, v in ct.items()]
        ct_list.sort(key = lambda a : -a[1])
        res = 0
        num_removed = 0
        for _, v in ct_list:
            num_removed += v
            res += 1
            if num_removed >= sz // 2:
                return res
        return res