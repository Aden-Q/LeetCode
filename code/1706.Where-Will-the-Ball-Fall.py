class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        # for each ball
        res = []
        for col in range(n):
            # for each level
            ans = col
            for row in range(m):
                if ans == 0 and grid[row][ans] == -1:
                    # blocked at the first col
                    ans = -1
                    break
                elif ans == n - 1 and grid[row][ans] == 1:
                    # blocked at the last col
                    ans = -1
                    break
                elif grid[row][ans] == 1 and grid[row][ans+1] == -1:
                    # blocked at a V shape
                    ans = -1
                    break
                elif grid[row][ans] == -1 and grid[row][ans-1] == 1:
                    # blocked at a V shape
                    ans = -1
                    break
                else:
                    # flow to the next level
                    if grid[row][ans] == 1:
                        ans += 1
                    else:
                        ans -= 1
            res.append(ans)
        return res