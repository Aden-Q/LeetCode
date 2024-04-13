class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1], reverse = True)
        res = 0
        for numBox, numUnit in boxTypes:
            if truckSize > numBox:
                res += numUnit * numBox
                truckSize -= numBox
            else:
                res += numUnit * truckSize
                break
        return res