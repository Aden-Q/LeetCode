class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        res = [[0] for _ in range(m)]
        for i in range(m):
            res[i] = original[n * i: n * (i+1)]
        return res