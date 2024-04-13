class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # a dp state can be described by 3 variables:
        # day: the day we are current at, 0-indexed for convenience
        # hold: whether we are holding the stock or not on the current day
        # k: number of transactions left to buy and sell stocks
        # the function returns the maximum profit we can get for the given state
        @cache
        def dp(day: int, hold: bool, k: int) -> int:
            if day == n:
                # no more days
                return 0
            if k == 0:
                # no more transactions, we can neither sell or buy any stock
                return 0

            # for the current day, if we are holding the stock, we have two choices:
            # 1. keep holding
            # 2. sell the stock at the current day's price
            # if we are not holding the stock at the current day, we have two choices:
            # 1. buy stock at current day's price
            # 2. do not buy stock
            if hold:
                return max(dp(day+1, True, k), prices[day] + dp(day+1, False, k-1))
            else:
                return max(-prices[day] + dp(day+1, True, k), dp(day+1, False, k))

        return dp(0, False, k)