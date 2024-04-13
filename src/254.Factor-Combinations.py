class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def dfs(n) -> List[List[int]]:
            if n == 1:
                return []

            res = deque()
            factor = 2
            while factor * factor <= n:
                if n % factor:
                    # n is not divisible by this factor
                    factor += 1
                    continue
                # this is a special case when the the comb only consists of 2 number, which cannot be derived from a recursive step
                res.append(deque([factor, n // factor]))
                prev_combs = dfs(n // factor)
                for comb in prev_combs:
                    if comb[0] < factor:
                        continue
                    comb.appendleft(factor)
                    res.append(comb)

                factor += 1
            
            return res

        return dfs(n)
