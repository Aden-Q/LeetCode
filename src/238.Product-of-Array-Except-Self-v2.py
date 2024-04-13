class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # ans[i] keeps the product of all members left to i, exclusive
        ans = [1] * n

        # keep ans as the left prefix product
        for i in range(1, n):
            ans[i] = ans[i-1] * nums[i-1]

        right_prod = 1

        for i in reversed(range(n)):
            ans[i] *= right_prod
            right_prod *= nums[i]

        return ans
