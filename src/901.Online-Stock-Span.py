class StockSpanner:
    def __init__(self):
        self.prices = []
        # store a jump index
        # jump[i] represents the most recent day who has a higher stock price is i - jump[i] (index)
        # so prices[i-jump[i]] > prices[i] and for  i-jump[i] < j < i, we have prices[j] <= prices[i]
        # if jump[i] = -1, then there's no such a previous day whose stock price is higher
        self.jump = []
        # both arrays keep growing in size

    def next(self, price: int) -> int:
        if not self.prices:
            self.prices.append(price)
            self.jump.append(-1)
            return 1

        # otherwise we need to jump
        idx = len(self.prices) - 1
        self.prices.append(price)
        self.jump.append(idx)
        
        while idx != -1 and self.prices[idx] <= price:
            # jump
            idx = self.jump[idx]
        
        self.jump[-1] = idx

        return len(self.jump) - self.jump[-1] - 1

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)