class Solution:
    def trailingZeroes(self, n: int) -> int:
        cnt_twos = 0
        cnt_fives = 0

        def countNum(num, d) -> int:
            cnt = 0
            while num % d == 0:
                cnt += 1
                num //= d

            return cnt

        for num in range(n, 0, -1):
            cnt_twos += countNum(num, 2)
            cnt_fives += countNum(num, 5)

        return min(cnt_twos, cnt_fives)
