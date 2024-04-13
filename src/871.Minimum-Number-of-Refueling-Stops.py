import heapq

class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # Greedy approach
        pq = []
        stations.append((target, float('inf')))
        
        res = 0
        currPos = 0
        currFuel = startFuel
        for location, fuel in stations:
            currFuel -= location - currPos
            while pq and currFuel < 0:
                # If the current Fuel is negative and there is some station we can fill up the gas
                currFuel += -heapq.heappop(pq)
                # One more station
                res += 1
            # If failed to fill up the gas
            if currFuel < 0:
                return -1
            # If succeed, push the current station into the heap
            heapq.heappush(pq, -fuel)
            # Update the location of the trunk
            currPos = location
        
        return res