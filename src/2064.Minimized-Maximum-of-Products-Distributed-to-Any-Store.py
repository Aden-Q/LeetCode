class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        m = len(quantities)
        left, right = sum(quantities) // n, max(quantities)

        # check whether ther's a distribution such that the number of products in any store is <= x
        def feasible(x) -> bool:
            idx = 0
            quantities_remaining = quantities[idx]
            for i in range(n):
                if idx >= m:
                    return True

                if quantities_remaining == 0:
                    quantities_remaining = quantities[idx]

                if x >= quantities_remaining:
                    idx += 1
                    quantities_remaining = 0
                else:
                    quantities_remaining -= x

            return False if quantities_remaining > 0 or idx < m else True

        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                # we want to find the minimum value
                right = mid
            else:
                left = mid + 1
        
        return right
