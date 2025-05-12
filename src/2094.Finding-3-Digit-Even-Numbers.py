class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        digits_counter = Counter(digits)

        for num in range(100, 1000):
            num_temp = num
            right = num_temp % 10
            num_temp = num_temp // 10
            mid = num_temp % 10
            num_temp = num_temp // 10
            left = num_temp % 10

            if right % 2 != 0:
                continue

            if Counter([left, mid, right]) <= digits_counter:
                ans.append(num)

        return ans
