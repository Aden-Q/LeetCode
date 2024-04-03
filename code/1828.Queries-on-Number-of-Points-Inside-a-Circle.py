class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        m, n = len(points), len(queries)
        ans = []
        for c_x, c_y, c_r in queries:
            cnt = 0
            for p_x, p_y in points:
                if (p_x - c_x) ** 2 + (p_y - c_y) ** 2 <= c_r ** 2:
                    cnt += 1

            ans .append(cnt)
        
        return ans
