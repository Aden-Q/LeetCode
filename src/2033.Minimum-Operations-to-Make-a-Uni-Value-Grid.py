class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        vals = []
        for row in grid:
            for e in row:
                vals.append(e)

        vals.sort()
        median = vals[len(vals) // 2]
        ops = 0
        for val in vals:
            if abs(median - val) % x != 0:
                return -1
            
            ops += abs(median - val) // x

        return ops
