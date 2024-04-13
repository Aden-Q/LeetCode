class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        curr_altitude = 0
        for g in gain:
            curr_altitude += g
            highest = max(highest, curr_altitude)
        
        return highest