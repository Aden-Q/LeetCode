class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.ans = []

        def dfs(remain, start, path):
            if remain == 0 and len(path) == k:
                self.ans.append(path[:])
                return
            if remain < 0 or len(path) == k:
                return
            
            for i in range(start, 10):
                path.append(i)
                dfs(remain-i, i+1, path)
                path.pop()

        dfs(n, 1, [])
        return self.ans
