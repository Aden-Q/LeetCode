class Solution:
    def backtracking(self, start, end, k, path, res):
        # base case
        if k == -1 and path:
            res.append(path.copy())
        for j in range(start, end+1):
            path.append(j)
            self.backtracking(j+1, end, k-1, path, res)
            path.pop()
        
    
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        self.backtracking(1, n, k-1, path, res)
        return res
        