class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        # given a time, check whether it's possible for all buses to complete at least totalTrips
        def canCompleteTrips(t) -> bool:
            cnt = 0
            for bus_trip_time in time:
                cnt += t // bus_trip_time
                if cnt >= totalTrips:
                    return True
            
            return False

        left, right = min(time) - 1, min(time) * totalTrips
        while left < right:
            mid = left + (right - left) // 2
            if canCompleteTrips(mid):
                right = mid
            else:
                left = mid + 1
        
        return right
