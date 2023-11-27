class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        currMin = arrays[0][0]
        currMax = arrays[0][-1]
        maxDist= 0

        for i in range(1, len(arrays)):
            rowMin= arrays[i][0]
            rowMax = arrays[i][-1]
            maxDist = max(maxDist, abs(currMin - rowMin), abs(currMin - rowMax), abs(currMax - rowMax), abs(currMax - rowMin))
            
            # update currMin and currMax
            currMin = min(currMin, rowMin)
            currMax = max(currMax, rowMax)

        return maxDist
