class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        # return True is the number of elements in the multiplication table less than num is >= k
        def feasible(num) -> bool:
            total_nums_less_than_num = 0
            for i in range(1, m + 1):
                total_nums_less_than_num += min(num // i, n)
                if total_nums_less_than_num >= k:
                    # early return
                    return True
            
            return False

        left, right = 1, m * n
        while left < right:
            mid = (right - left) // 2 + left
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
