class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        jobs = list(zip(startTime, endTime, profit))
        # first we sort jobs by their starting time
        jobs.sort()

        # returns the maximum profit we can get by using jobs[idx:], without overlapping
        @cache
        def dp(idx):
            nonlocal jobs
            if idx == len(jobs):
                # no jobs left can be chosen
                return 0
            
            # for jobs[idx], we can 2 choices, either we choose this job, or we do not choose this job
            # compare the relative profit gain and choose the greater one
            # we do not choose the current job
            max_profit = dp(idx+1)
            # choose the current job, we need to find the next idx
            next_idx = bisect.bisect_left(jobs, jobs[idx][1], key=lambda x: x[0])
            max_profit = max(max_profit, jobs[idx][2] + dp(next_idx))

            return max_profit

        return dp(0)
