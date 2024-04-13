from collections import deque, defaultdict

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        ht = defaultdict(deque)
        
        for row in range(m):
            for col in range(n):
                ht[row - col].append(mat[row][col])
        
        # Timesort
        for key in ht.keys():
            ht[key] = deque(sorted(ht[key]))
            
        for row in range(m):
            for col in range(n):
                val = ht[row - col].popleft()
                mat[row][col] = val
        
        return mat