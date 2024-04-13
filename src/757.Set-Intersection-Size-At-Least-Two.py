from sortedcontainers import SortedSet

class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        containing_set = SortedSet()
        # sort by end
        intervals.sort(key=lambda x: x[1])
        for start, end in intervals:
            left = containing_set.bisect_left(start)
            right = containing_set.bisect_right(end)
            if right == left + 1:
                if end not in containing_set:
                    containing_set.add(end)
                else:
                    containing_set.add(end-1)
            elif right == left:
                containing_set.add(end)
                containing_set.add(end-1)

        return len(containing_set)
