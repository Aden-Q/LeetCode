class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        n = len(nums)
        # next_smaller[i] is the index of the next smaller element of nums[i]
        next_smaller = [n] * n
        mono_inc_stack = []
        for i in range(n):
            while mono_inc_stack and nums[mono_inc_stack[-1]] > nums[i]:
                next_smaller[mono_inc_stack.pop()] = i
            
            mono_inc_stack.append(i)

        prev_smaller = [-1] * n
        mono_inc_stack = []
        for i in reversed(range(n)):
            while mono_inc_stack and nums[mono_inc_stack[-1]] > nums[i]:
                prev_smaller[mono_inc_stack.pop()] = i
            
            mono_inc_stack.append(i)

        # prefix_sum[k] = sum of nums[i] for i < k
        prefix_sum = [0] * (n + 1)
        for i in range(n):
            prefix_sum[i+1] = prefix_sum[i] + nums[i]

        max_min_prod = 0
        for i in range(n):
            left, right = prev_smaller[i] + 1, next_smaller[i] - 1
            sum_of_subarray = prefix_sum[right+1] - prefix_sum[left]
            min_prod = sum_of_subarray * nums[i]
            max_min_prod = max(max_min_prod, min_prod)

        return max_min_prod % (10 ** 9 + 7)
