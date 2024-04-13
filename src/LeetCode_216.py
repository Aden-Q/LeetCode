class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []  # a single path
        res = []  # store paths
        def backtracking(n, start):
            # check whether a solution is reached
            if len(path) == k and n == 0:
                res.append(path[:])
                return
            # pruning
            elif n < 0 or len(path) == k:
                return
            # process a single
            for i in range(start, 10):
                path.append(i)
                backtracking(n-i, i+1)
                path.pop()  # revert to the original state
        # invoke
        backtracking(n, 1)
        
        return res

        
if __name__ == '__main__':
    test = Solution()
    test.combinationSum3(7, 3)