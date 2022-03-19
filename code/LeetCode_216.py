class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []  # a single path
        res = []  # store final solution
        def backtracking(n, start):
            # get a solution
            if len(path) == k and n == 0:
                res.append(path[:])
                return
            elif n < 0:
                return
            # process a single node and run backtracking
            for i in range(start, 10):
                path.append(i)
                backtracking(n-i, i+1)
                path.pop()  # revert
        # invoke
        backtracking(n, 1)
        
        return res

        
if __name__ == '__main__':
    test = Solution()
    test.combinationSum3(7, 3)