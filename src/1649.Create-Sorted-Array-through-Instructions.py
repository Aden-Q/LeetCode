from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        totalCost = 0
        mod = 10 ** 9 + 7
        sl = SortedList()
        for num in instructions:
            totalCost += min(sl.bisect_left(num), len(sl) - sl.bisect_right(num))
            totalCost = totalCost % mod
            sl.add(num)

        return totalCost
