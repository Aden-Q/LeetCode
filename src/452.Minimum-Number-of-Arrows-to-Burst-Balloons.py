class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        idx = 0
        arrow_count = 0
        print(points)
        while idx < len(points):
            arrow = points[idx][1]
            arrow_count += 1
            while idx < len(points) and points[idx][0] <= arrow:
                idx += 1
        return arrow_count