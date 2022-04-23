import math

class Solution:
    def countHours(self, piles, speed) -> int:
        count = 0
        for pile in piles:
            count += math.ceil(pile / speed)
        return count
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        
        while left < right:
            mid = (left + right) // 2
            if self.countHours(piles, mid) < h:
                # shrink right boundary
                right = mid
            elif self.countHours(piles, mid) == h:
                # shrink right boundary
                right = mid
            else:
                left = mid + 1
        return left