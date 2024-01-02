class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        # the number of rows: the frequency of the most frequent number
        counter = Counter(nums)
        max_freq = max(counter.values())
        res = [[] for _ in range(max_freq)]
        for key, val in counter.items():
            for i in range(val):
                res[i].append(key)

        return res
