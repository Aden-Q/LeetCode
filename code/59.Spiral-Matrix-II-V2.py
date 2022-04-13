class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        upper_bound = 0
        lower_bound = n - 1
        left_bound = 0
        right_bound = n - 1
        num = 1
        while num <= n * n:
            # from left to right
            for i in range(left_bound, right_bound + 1):
                res[upper_bound][i] = num
                num += 1
            upper_bound += 1    
            # from top to bottom
            for i in range(upper_bound, lower_bound + 1):
                res[i][right_bound] = num
                num += 1
            right_bound -= 1
            # from right to left
            for i in range(right_bound, left_bound - 1, -1):
                res[lower_bound][i] = num
                num += 1
            lower_bound -= 1
            # from bottom to top
            for i in range(lower_bound, upper_bound - 1, -1):
                res[i][left_bound] = num
                num += 1
            left_bound += 1
        return res