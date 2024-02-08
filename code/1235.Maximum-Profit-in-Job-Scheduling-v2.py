class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        # first we sort jobs by their starting time
        jobs.sort()

        dp = [0] * (len(jobs) + 1)
        for i in range(len(jobs) -1, -1, -1):
            # skip the current job
            dp[i] = dp[i+1]
            # schedule the current job
            next_idx = bisect.bisect_left(jobs, jobs[i][1], lo=i+1, key=lambda x: x[0])
            dp[i] = max(dp[i], dp[next_idx] + jobs[i][2])

        return dp[0]
