class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        # calculate the number of subarrays that satisfy the condition between nums[start]
        # and nums[end] when all elements are between minK and maxK
        def calSubarraysHelper(start, end) -> int:
            ans = 0
            most_recent_minK_idx = start - 1
            most_recent_maxK_idx = start - 1
            for i in range(start, end+1):
                if nums[i] == minK:
                    most_recent_minK_idx = i
                if nums[i] == maxK:
                    most_recent_maxK_idx = i
                
                ans += max(0, min(most_recent_minK_idx, most_recent_maxK_idx) - start + 1)

            return ans

        ans = 0
        start_idx = end_idx = 0
        while start_idx < len(nums):
            if minK <= nums[start_idx] <= maxK:
                # found a part
                end_idx = start_idx
                while end_idx + 1 < len(nums) and minK <= nums[end_idx + 1] <= maxK:
                    end_idx += 1
                ans += calSubarraysHelper(start_idx, end_idx)

                start_idx = end_idx + 1
            else:
                start_idx += 1

        return ans
