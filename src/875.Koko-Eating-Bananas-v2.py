class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Search space: [1, max(piles)]
        left, right = 1, max(piles)
        
        while left < right:
            mid = (left + right) // 2
            h_needed = 0
            
            for pile in piles:
                h_needed += math.ceil(pile / mid)
                if h_needed > h:
                    break
            
            if h_needed > h:
                left = mid + 1
            else:
                right = mid
        
        return left