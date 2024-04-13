class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)

        # returns the maximum number of points we can get if we start from questions[start], either by solving it or skip it
        @cache
        def dp(start) -> int:
            if start >= n:
                return 0
            
            points, skip = questions[start]
            # if we solve the current problem
            points += dp(start + skip + 1)

            return max(points, dp(start + 1))

        return dp(0)
