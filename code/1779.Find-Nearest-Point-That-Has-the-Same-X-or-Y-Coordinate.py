class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        min_dist = float('inf')
        min_idx = -1
        for idx, point in enumerate(points):
            px, py = point
            if px == x or py == y:
                # valid point
                cur_dist = abs(px - x) + abs(py - y)
                if cur_dist < min_dist:
                    min_dist = cur_dist
                    min_idx = idx
        return min_idx