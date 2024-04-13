class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # return true if for the given divisor, the sum is at most threshold
        def feasible(divisor) -> bool:
            total_sum = 0
            for num in nums:
                total_sum += math.ceil(num / divisor)
                # early return
                if total_sum > threshold:
                    return False

            return True

        left, right = 1, max(nums) + 1
        while left < right:
            mid = left + (right - left) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
