class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # a running in-air lookup table
        dt = set(mat[0])
        m, n = len(mat), len(mat[0])
        for row in range(1, m):
            next_dt = set()
            for col in range(n):
                if mat[row][col] in dt:
                    next_dt.add(mat[row][col])
            dt = next_dt
        
        return min(dt) if dt else -1
