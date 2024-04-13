from sortedcontainers import SortedDict

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        n = len(chargeTimes)
        sd = SortedDict()
        left = right = 0
        max_robots = 0
        sum_running_costs = 0
        
        while right < n:
            sd[chargeTimes[right]] = sd.get(chargeTimes[right], 0) + 1
            sum_running_costs += runningCosts[right]
            
            while left <= right and sd.peekitem()[0] + (right - left + 1) * sum_running_costs > budget:
                sd[chargeTimes[left]] -= 1
                if sd[chargeTimes[left]] == 0:
                    del sd[chargeTimes[left]]
                sum_running_costs -= runningCosts[left]
                left += 1

            max_robots = max(max_robots, right - left + 1)
            right += 1

        return max_robots
