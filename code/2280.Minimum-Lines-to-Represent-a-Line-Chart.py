class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        stockPrices.sort(key = lambda a: a[0])
        idx = 0
        n = len(stockPrices)
        if n == 1:
            return 0
        count = 1
        mode = (stockPrices[1][1] - stockPrices[0][1])
        mul = (stockPrices[1][0] - stockPrices[0][0])
        while idx < n - 1:
            next_mode = (stockPrices[idx+1][1] - stockPrices[idx][1])
            next_mul = (stockPrices[idx+1][0] - stockPrices[idx][0])
            if  next_mode * mul != mode * next_mul:
                mode = next_mode
                mul = next_mul
                count += 1
            idx += 1
        return count