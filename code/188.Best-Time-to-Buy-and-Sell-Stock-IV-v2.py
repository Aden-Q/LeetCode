class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # a dp state can be described by 3 variables:
        # day: the day we are current at, 0-indexed for convenience
        # hold: whether we are holding the stock or not on the current day
        # k: number of transactions left to buy and sell stocks
        # the function returns the maximum profit we can get for the given state
        dp = [[[0] * (k+1) for _ in range(2)] for _ in range(n+1)]
        for day in reversed(range(n)):
            for k_iter in range(1, k+1):
                # when hold == False
                dp[day][0][k_iter] = max(-prices[day] + dp[day+1][1][k_iter], dp[day+1][0][k_iter])
                # when hold == True
                dp[day][1][k_iter] = max(dp[day+1][1][k_iter], prices[day] + dp[day+1][0][k_iter-1])

        return dp[0][0][k]