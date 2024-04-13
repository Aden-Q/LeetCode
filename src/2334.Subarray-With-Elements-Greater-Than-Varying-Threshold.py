class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        n = len(nums)
        # use a monotonic increasing stack to find the next smaller element for every index
        mono_inc_stack = []
        next_smaller = [n] * n
        for idx, num in enumerate(nums):
            while mono_inc_stack and nums[mono_inc_stack[-1]] > num:
                next_smaller[mono_inc_stack[-1]] = idx
                mono_inc_stack.pop()

            mono_inc_stack.append(idx)

        # use a monotonic stack to find the first prev smaller element for every index
        mono_inc_stack = []
        prev_smaller = [-1] * n
        for idx in reversed(range(n)):
            num = nums[idx]
            while mono_inc_stack and nums[mono_inc_stack[-1]] > num:
                prev_smaller[mono_inc_stack[-1]] = idx
                mono_inc_stack.pop()

            mono_inc_stack.append(idx)

        # now for every index, greedy select the longest possible subarray
        for idx in range(n):
            # inclusive
            left, right = prev_smaller[idx] + 1, next_smaller[idx] - 1
            # the minimm element in nums[left:right+1] is nums[idx]
            k = right - left + 1
            if nums[idx] > threshold / k:
                return k

        return -1
