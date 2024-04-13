class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions = [(val, idx) for idx, val in enumerate(potions)]
        potions.sort()
        spells = [(val, idx) for idx, val in enumerate(spells)]
        spells.sort()
        left = 0
        right = len(potions) - 1
        res = [0] * len(spells)
        while left < len(spells):
            while right >= 0 and spells[left][0] * potions[right][0] >= success:
                right -= 1
            res[spells[left][1]] = max(res[left], len(potions) - right - 1)
            left += 1
        
        return res
            