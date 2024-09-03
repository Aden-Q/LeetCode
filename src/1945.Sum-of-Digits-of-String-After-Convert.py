class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def sum_digits(n) -> int:
            ans = 0
            while n:
                ans += n % 10
                n = n // 10

            return ans

        n = ""
        for c in s:
            n += str(ord(c) - ord("a") + 1)

        n = int(n)
        for _ in range(k):
            n = sum_digits(n)

        return n
