class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        # a dp state can be described by 3 variables:
        # day: the day we are current at, 0-indexed for convenience
        # hold: whether we are holding the stock or not on the current day
        # k: number of transactions left to buy and sell stocks
        # the function returns the maximum profit we can get for the given state
        prev_day = [[0] * (k+1) for _ in range(2)]
        curr_day = [[0] * (k+1) for _ in range(2)]
        for day in reversed(range(n)):
            for k_iter in range(1, k+1):
                # when hold == False
                curr_day[0][k_iter] = max(-prices[day] + prev_day[1][k_iter], prev_day[0][k_iter])
                # when hold == True
                curr_day[1][k_iter] = max(prev_day[1][k_iter], prices[day] + prev_day[0][k_iter-1])
            prev_day, curr_day = curr_day, prev_day

        return prev_day[0][k]