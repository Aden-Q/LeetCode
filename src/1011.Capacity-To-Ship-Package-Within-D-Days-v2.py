class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # we need to search for the minimum value that satisfies the condition
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (right - left) // 2 + left
            # test whether mid is workable solution
            total_days = 1
            total_weights = 0
            for weight in weights:
                if total_weights + weight > mid:
                    total_days += 1
                    total_weights = 0

                    if total_days > days:
                        break

                total_weights += weight

            if total_days <= days:
                right = mid
            else:
                left = mid + 1

        return left
