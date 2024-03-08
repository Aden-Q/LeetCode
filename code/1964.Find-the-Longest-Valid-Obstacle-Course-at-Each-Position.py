class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        # this is just a LIS problem
        n = len(obstacles)
        ans = [1] * n
        window = []
        for i in range(n):
            obstacle = obstacles[i]
            insert_idx = bisect.bisect_right(window, obstacle)
            if insert_idx == len(window):
                window.append(obstacle)
            else:
                window[insert_idx] = obstacle

            ans[i] = insert_idx + 1

        return ans
