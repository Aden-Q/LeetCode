class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = [(idx, x**2 + y**2) for idx, (x, y) in enumerate(points)]
        dist.sort(key = lambda x : x[1])
        return [points[i] for i, _ in dist[:k]]