class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        # total number of ways to paint a single row
        max_val = 3**3

        # all valid ways
        p = []

        def toArr(mask):
            arr = []
            for _ in range(3):
                arr.append(mask % 3)
                mask //= 3

            return arr

        for val in range(max_val):
            arr = toArr(val)
            if arr[0] == arr[1] or arr[1] == arr[2]:
                continue

            p.append(val)

        from collections import defaultdict

        d = defaultdict(list)

        for prev in p:
            arr_prev = toArr(prev)
            for curr in p:
                arr_curr = toArr(curr)
                valid = True

                for i in range(3):
                    if arr_prev[i] == arr_curr[i]:
                        valid = False
                        break

                if valid:
                    d[prev].append(curr)

        dp = [[0] * max_val for _ in range(n + 1)]

        for val in p:
            dp[1][val] = 1

        for row in range(2, n + 1):
            for prev in p:
                for curr in d[prev]:
                    dp[row][curr] = (dp[row][curr] + dp[row - 1][prev]) % mod

        return sum(dp[n]) % mod
