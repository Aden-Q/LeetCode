class Solution:
    def countOdds(self, low: int, high: int) -> int:
        state = low % 2  + high % 2
        if state == 0:
            return (high - low) // 2
        else:
            return (high - low) // 2 + 1