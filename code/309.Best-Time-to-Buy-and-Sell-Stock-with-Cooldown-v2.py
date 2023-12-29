class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n+2)]

        prev_day = [0, 0]
        prev_prev_day = [0, 0]
        curr_day = [0, 0]
        for day in reversed(range(n)):
            # holding
            curr_day[1] = max(prev_day[1], prices[day] + prev_prev_day[0])
            # not holding
            curr_day[0] = max(prev_day[0], -prices[day] + prev_day[1])

            prev_day, prev_prev_day, curr_day = curr_day, prev_day, prev_prev_day

        # start from the first day, without holding the stock
        return prev_day[0]