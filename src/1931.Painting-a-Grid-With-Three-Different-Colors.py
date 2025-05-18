class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        mod = 10**9 + 7
        # enumerate row in ternary format
        max_val = 3**m
        p = []

        def toArr(mask):
            arr = []
            for _ in range(m):
                arr.append(mask % 3)
                mask //= 3

            return arr

        for val in range(max_val):
            arr = toArr(val)
            valid = True
            for i in range(m - 1):
                if arr[i] == arr[i + 1]:
                    valid = False
                    break

            if valid:
                p.append(val)

        from collections import defaultdict

        d = defaultdict(list)

        for prev in p:
            arr_prev = toArr(prev)

            for curr in p:
                arr_curr = toArr(curr)
                valid = True
                for a, b in zip(arr_prev, arr_curr):
                    if a == b:
                        valid = False
                        break

                if valid:
                    d[prev].append(curr)

        dp = [[0] * max_val for _ in range(n + 1)]
        for val in p:
            dp[1][val] = 1

        for col in range(2, n + 1):
            for prev in p:
                for curr in d[prev]:
                    dp[col][curr] = (dp[col][curr] + dp[col - 1][prev]) % mod

        return sum(dp[n]) % mod
