class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        cur = [1, 1]
        next_row = cur
        for i in range(1, rowIndex):
            next_row = [1]
            for j in range(i):
                next_row.append(cur[j] + cur[j+1])
            next_row.append(1)
            cur = next_row
        return next_row