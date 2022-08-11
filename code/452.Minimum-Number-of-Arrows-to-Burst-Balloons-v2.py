class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x : x[1])
        cnt = 1
        
        p_end = points[0][1]
        for point in points[1:]:
            if point[0] > p_end:
                cnt += 1
                p_end = point[1]
        
        return cnt