class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # we can search for n
        # given a number, check how many distinct numbers we have that <= num
        # if the number >=n returns True, otherwise returns False
        # then it becomes a binary search problem
        def feasible(num):
            num_integers = 0
            num_integers += num // a
            num_integers += num // b
            num_integers += num // c
            num_integers -= num // ab
            num_integers -= num // ac
            num_integers -= num // bc
            num_integers += num // abc
            
            return num_integers >= n

        left, right = 1, 10 ** 10
        ab = a * b // gcd(a, b)
        ac = a * c // gcd(a, c)
        bc = b * c // gcd(b, c)
        abc = a * bc // gcd(a, bc)
        while left < right:
            mid = (right - left) // 2 + left
            if feasible(mid):
                right = mid
            else:
                left = mid + 1

        return left
