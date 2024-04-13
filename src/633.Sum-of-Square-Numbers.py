class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while 2 * a * a <= c:
            left = a
            right = int(math.sqrt(c))
            while left <= right:
                mid = (left + right) // 2
                cur_sum = mid * mid + a * a
                if cur_sum == c:
                    return True
                elif cur_sum < c:
                    left = mid + 1
                else:
                    right = mid - 1
            a += 1
        return False
            