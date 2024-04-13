class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        total_drink = numBottles
        num_empty = numBottles
        while num_empty >=  numExchange:
            num_empty -= numExchange
            numExchange += 1
            total_drink += 1
            num_empty += 1
        
        return total_drink
