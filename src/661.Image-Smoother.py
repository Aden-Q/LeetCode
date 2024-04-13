class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])

        def calAverage(row_min, row_max, col_min, col_max):
            culSum = 0
            cnt = 0

            for row in range(row_min, row_max + 1):
                for col in range(col_min, col_max + 1):
                    if 0 <= row < m and 0 <= col < n:
                        cnt += 1
                        culSum += img[row][col]
            if cnt == 0:
                return 0

            return culSum // cnt
        
        res = copy.deepcopy(img)
        for row in range(m):
            for col in range(n):
                # inclusive range
                row_min, row_max = row - 1, row + 1
                col_min, col_max = col - 1, col + 1
                res[row][col] = calAverage(row_min, row_max, col_min, col_max)
        
        return res
