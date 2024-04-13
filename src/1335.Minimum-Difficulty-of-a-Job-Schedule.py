class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)
        if n < d:
            # early termination from an edge case here so we don't need to worry about the following return path
            return -1

        job_diff_suffix_sum = [0] * n
        job_diff_suffix_sum[-1] = jobDifficulty[-1]
        for i in range(n-2, -1, -1):
            job_diff_suffix_sum[i] = job_diff_suffix_sum[i+1] + jobDifficulty[i]

        # return the minimum difficulty to schedule jobs starting from 'start' as an index of the jobDifficulty
        # and we want  to finish all jobs exactly for d days
        # returns the result as an int
        @cache
        def dp(start, d) -> int:
            if d < 0:
                # impossible schedule case 1
                return math.inf
            if n - start < d:
                # impossibly schedule case 2
                return math.inf

            if n - start == d:
                # base case 3: when there are exactly d jobs left, we must finish one at day
                # here we can optimize it using a suffix sum
                return job_diff_suffix_sum[start] if d > 0 else 0

            # otherwise we try all possible cuts
            # to schedule job for the current day
            min_difficulty = math.inf
            curr_day_max_difficulty = jobDifficulty[start]
            for end in range(start, n):
                curr_day_max_difficulty = max(curr_day_max_difficulty, jobDifficulty[end])
                min_difficulty = min(min_difficulty, curr_day_max_difficulty + dp(end+1, d-1))

            return min_difficulty

        # we want to finish all jobs in d days
        return dp(0, d)
