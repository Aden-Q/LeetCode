class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        upper_bound = sum(ribbons) // k
        upper_bound = max(upper_bound, max(ribbons))
        lower_bound = 1

        # perform binary search
        left, right = lower_bound, upper_bound
        while left <= right:
            mid = (left + right) >> 1
            num_ribbons = sum(map(lambda x: x // mid, ribbons))
            if num_ribbons >= k:
                left = mid + 1
            else:
                right = mid - 1

        return right