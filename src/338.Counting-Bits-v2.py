class Solution:
    def countBits(self, n: int) -> List[int]:
        # generate [2^{k} - 2^{k+1} - 1]
        # from [0, 2^{k})
        # initially use [0, 2), which 2 = 2^{1}
        # b = 2^{k}
        b = 1
        res = [0 for _ in range(n+1)]

        while b <= n + 1:
            for x in range(b):
                if x + b > n:
                    break
                res[x+b] = res[x] + 1
            b *= 2
        
        return res
