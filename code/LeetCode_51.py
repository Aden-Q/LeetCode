class Solution:
    def solveNQueens(self, n: int):
        path = [] # each path consists of n digits, denoting queen's position on each row
        res = []
        used = [False] * n  # indicating whether the slots in occupy column-wise
        def convert(s):
            size = len(s)
            res = [[] * size] * size
            for i in range(size):
                res[i] = (s[i]) * '.' + 'Q' + (size-s[i]-1) * '.'
            return res

        def is_valid(path, i):
            # check column
            if used[i]:
                return False
            # check diagnal
            for j in range(len(path)):
                if path[-j-1] - i == j+1 or path[-j-1] - i == -j-1:
                    return False
            return True
        
        def backtracking(n):
            nonlocal path, res, used
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if is_valid(path, i):
                    used[i] = True
                    path.append(i)
                    backtracking(n)
                    path.pop()
                    used[i] = False
            
        backtracking(n)
        # convert output
        for i in range(len(res)):
            res[i] = convert(res[i])
        return res
        
if __name__ == '__main__':
    test = Solution()
    res = test.solveNQueens(4)
    print(res)