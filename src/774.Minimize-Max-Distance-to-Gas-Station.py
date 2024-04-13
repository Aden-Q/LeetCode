class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        distances = [(stations[i] - stations[i-1]) for i in range(1, len(stations))]

        # we search for the answer
        # search boundary [left, right)
        left, right = min(distances) / k + 1e-6, max(distances)
        while left + 1e-6 < right:
            mid = (right - left) / 2 + left
            # now we verify whether mid is possible
            # cheeck in order to achieve mid, how many stations need to be added
            num_stations = 0
            for dist in distances:
                # I need to add those number of stations in order to satisfy mid
                if dist > mid:
                    num_stations += int((dist + 1e-6) / mid)
                    if num_stations > k:
                        break
            if num_stations > k:
                # unworkable
                left = mid + 1e-6
            else:
                right = mid

        return left
