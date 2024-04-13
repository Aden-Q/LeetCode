class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mod = 10 ** 9 + 7

        @cache
        def dfs(n, remain) -> int:
            if n * k < remain:
                return 0
            if n * 1 > remain:
                return 0
            if n == 0 and remain == 0:
                return 1

            # otherwise we roll the first indices and recursively solve the problem
            res = 0
            for i in range(1, k+1):
                res += dfs(n-1, remain - i)
                res = res % (mod)

            return res

        return dfs(n, target)