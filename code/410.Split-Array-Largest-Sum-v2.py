class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # we need to search for the answer and divide the array accordingly
        left, right = max(nums), sum(nums) + 1
        # search space: [left, right)
        while left < right:
            mid = (right - left) // 2 + left
            num_subarrays = 1
            curr_sum = 0
            for num in nums:
                if curr_sum + num > mid:
                    # oh, we cannot do this, we must start a new split
                    num_subarrays += 1
                    curr_sum = 0

                curr_sum += num

            if num_subarrays > k:
                # the current value is not workable, we must increase it
                left = mid + 1
            else:
                right = mid
        
        return right
