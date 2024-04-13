class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        first_min, second_min = prices[0], prices[1]
        if first_min > second_min:
            first_min, second_min = second_min, first_min

        for i in range(2, len(prices)):
            if prices[i] < first_min:
                first_min, second_min = prices[i], first_min
            elif prices[i] < second_min:
                first_min, second_min = first_min, prices[i]
        
        if first_min + second_min > money:
            return money
        
        return money - first_min - second_min