"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        OPEN, CLOSED = 1, 0
        events = []
        for e in schedule:
            for interval in e:
                events.append((interval.start, OPEN))
                events.append((interval.end, CLOSED))

        events.sort()
        ans = []
        num_open = 0
        prev = None

        for event in events:
            if num_open == 0 and prev != None and prev != event[0]:
                ans.append(Interval(prev, event[0]))

            if event[1] == OPEN:
                num_open += 1
            else:
                num_open -= 1

            if num_open == 0:
                prev = event[0]

        return ans