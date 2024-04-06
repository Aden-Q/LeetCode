from sortedcontainers import SortedList

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        sl = SortedList(changed)
        ans = []
        while sl:
            not_doubled = sl[0]
            doubled = 2 * not_doubled
            sl.remove(not_doubled)
            if doubled not in sl:
                return []
            sl.remove(doubled)
            ans.append(not_doubled)

        return ans
