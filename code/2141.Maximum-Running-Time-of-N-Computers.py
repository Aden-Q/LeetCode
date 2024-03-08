class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse=True)
        live = batteries[:n]
        live.sort()
        extra = sum(batteries[n:])

        for i in range(n-1):
            if extra >= (i + 1) * (live[i+1] - live[i]):
                extra -= (i + 1) * (live[i+1] - live[i])
            else:
                return live[i] + extra // (i+1)

        return live[-1] + extra // n
