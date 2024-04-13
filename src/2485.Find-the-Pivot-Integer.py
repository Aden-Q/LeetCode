class Solution:
    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        total_sum = (1 + n) * n // 2
        # looking for k such that sum (1+k) * k / 2 = (1 + n) * n / 2 - (1+k) * k / 2 + k

        while left <= right:
            mid = (left + right) // 2
            left_sum = (1 + mid) * mid // 2
            right_sum = total_sum - left_sum + mid
            if left_sum == right_sum:
                return mid
            elif left_sum < right_sum:
                left = mid + 1
            else:
                right = mid - 1
        
        return -1
