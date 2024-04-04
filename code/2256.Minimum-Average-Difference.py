class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        if start < goal:
            start, goal = goal, start
        start = bin(start)[2:]
        goal = bin(goal)[2:]
        goal = (len(start) - len(goal)) * '0' + goal
        count = 0
        for i in range(len(start)):
            if start[i] != goal[i]:
                count += 1
        return count