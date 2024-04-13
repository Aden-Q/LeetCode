class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        # dp[k][0] represents the maximum net gain if I have the stock on the k_th day
        # dp[k][1] represents the maximum net gain if I don't have the stock on the k_th day (either means I sell it, or I don't buy it)
        prev_hold = -prices[0]
        prev_free = 0
    
        # dp[i][0] = max(dp[i-1][0], dp[i-1][1] - prices[i])
        # dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i] - fee)
        for i in range(1, n):
            curr_hold = max(prev_hold, prev_free - prices[i])
            curr_free = max(prev_free, prev_hold + prices[i] - fee)
            prev_hold, prev_free = curr_hold, curr_free

        return prev_free
