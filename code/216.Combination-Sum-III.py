class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        used = [False] * 10
        res = []
        def backtracking(cur_sum, k, n, start):
            if cur_sum > n:
                return
            if k == 0:
                if cur_sum == n:
                    res.append(path[:])
                return
            for i in range(start, 10):
                if used[i] == False:
                    path.append(i)
                    used[i] = True
                    backtracking(cur_sum + i, k-1, n, i+1)
                    used[i] = False
                    path.pop()
            return
        backtracking(0, k, n, 1)
        return res