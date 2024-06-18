class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        n = len(difficulty)
        indices = list(range(n))

        indices.sort(key=lambda x: difficulty[x])

        max_so_far = [0] * n
        max_curr = 0

        for i in range(n):
            max_curr = max(max_curr, profit[indices[i]])
            max_so_far[i] = max_curr

        res = 0
        for w in worker:
            idx = bisect.bisect_right(indices, w, key=lambda x: difficulty[x]) - 1
            if idx >= 0:
                res += max_so_far[idx]

        return res
