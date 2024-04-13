class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m * k:
            return -1

        # otherwise it's always possible
        # we need to search for the number of days and find the minimum
        def feasible(days) -> bool:
            num_bouquets = 0
            total_flowers = 0
            for flower in bloomDay:
                if flower > days:
                    # this flower never bloom within the given days, reset
                    total_flowers = 0
                else:
                    total_flowers += 1
                    if total_flowers == k:
                        total_flowers = 0
                        num_bouquets += 1
                        if num_bouquets == m:
                            return True

            return False

        left, right = min(bloomDay), max(bloomDay)
        while left < right:
            mid = (right - left) // 2 + left
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
