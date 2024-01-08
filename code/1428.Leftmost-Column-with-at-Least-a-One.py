# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        # we can perform binary search
        rows, cols = binaryMatrix.dimensions()
        def getNumOnes(col: int) -> int:
            ans = 0
            for row in range(rows):
                if binaryMatrix.get(row, col) == 1:
                    ans += 1
            
            return ans

        # [left, right)        
        left, right = 0, cols
        while left < right:
            mid = ((right - left) >> 1) + left
            if getNumOnes(mid) >= 1:
                right = mid
            else:
                left = mid + 1

        return right if right < cols else -1
