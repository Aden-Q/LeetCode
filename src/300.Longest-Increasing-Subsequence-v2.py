class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # monotonic increasing stack
        n = len(nums)
        sub = [nums[0]]

        for i in range(1, n):
            if nums[i] > sub[-1]:
                sub.append(nums[i])
            else:
                idx = bisect.bisect_left(sub, nums[i])
                sub[idx] = nums[i]

        return len(sub)
