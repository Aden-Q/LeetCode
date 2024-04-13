class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        n = len(spells)
        m = len(potions)
        potions.sort()
        ans = [0] * n
        for i in range(n):
            target = success / spells[i]
            ans[i] = m - bisect.bisect_left(potions, target)

        return ans