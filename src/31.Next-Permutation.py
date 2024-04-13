class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # monotonic increasing stack, from the end to start
        # only store index to save space and we use the index for dereference
        # the monotonic is used to quickly index the target number to swap with
        stack = []
        for idx in range(len(nums)-1, -1, -1):
            # the first time we see a decreasing sequence, we can rearrange and return
            if stack and nums[idx] < nums[stack[-1]]:
                while stack and nums[idx] < nums[stack[-1]]:
                    target_idx = stack.pop()

                # swap nums[target_idx] and nums[idx]

                nums[idx], nums[target_idx] = nums[target_idx], nums[idx]
                # the next thing we need to do is sorting nums[idx+1] ascendingly in place, we can simply reverse this sublist, due to the nature of monotonic increasing stack
                left = idx+1
                right = len(nums) - 1
                while left < right:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right -= 1
                return
            # if no decreasing sequence found, continue
            stack.append(idx)

        # if we don't return from the loop, then the given input must be the last permutation
        # we return the first permutaion instead
        nums.reverse()
