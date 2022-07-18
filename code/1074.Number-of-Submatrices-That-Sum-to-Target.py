from collections import defaultdict

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        ps = [[0] * (n+1) for _ in range(m+1)]
        
        # calculate prefix sum
        for r in range(m):
            for c in range(n):
                ps[r+1][c+1] = ps[r][c+1] + ps[r+1][c] - ps[r][c] + matrix[r][c]
                
        cnt = 0
        # calculate sum and compare it with the target
        for r1 in range(m):
            for r2 in range(r1, m):
                h = defaultdict(int)
                h[0] = 1
                for c in range(n):
                    cur_sum = ps[r2+1][c+1] - ps[r1][c+1]
                    cnt += h[cur_sum - target]
                    h[cur_sum] += 1
        return cnt
        