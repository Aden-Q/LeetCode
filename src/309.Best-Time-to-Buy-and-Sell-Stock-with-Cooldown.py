class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        # return the maximum profit we can get start from some trading day
        @cache
        def dp(day: int, hold: bool) -> int:
            if day >= n:
                return 0

            # if we current hold the stock, we have 2 choices:
            # 1. we keep holding
            # 2. we sell it, then tomorrow is a cooldown day for which we can do nothing, so we need to skip tomorrow
            # if we are not holding the stock, we have 2 choices:
            # 1. we do nothing
            # 2. we buy the stock at the current day's price
            if hold:
                return max(dp(day+1, True), prices[day] + dp(day+2, False))
            else:
                return max(dp(day+1, False), -prices[day] + dp(day+1, True))

        # start from the first day, without holding the stock
        return dp(0, False)