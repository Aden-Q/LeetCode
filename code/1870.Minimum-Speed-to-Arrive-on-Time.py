class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        # givena train speed, checks whether we can reach the office within the given time 'hour'
        def feasible(speed) -> bool:
            total_hour = 0
            for i in range(len(dist) - 1):
                total_hour += math.ceil(dist[i] / speed)
                if total_hour > hour:
                    return False

            # the last train    
            total_hour += dist[-1] / speed
            return total_hour <= hour

        if len(dist) - 1 >= hour:
            return -1

        max_val = max(dist) * 100 + 1
        left, right = 1, max_val
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return right if right < max_val else -1
