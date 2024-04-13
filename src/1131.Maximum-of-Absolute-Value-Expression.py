class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # arr1[i] + arr2[i] + i
        # arr1[i] - arr2[i] + i
        # arr1[i] + arr2[i] - i
        # arr1[i] - arr2[i] - i
        nums = [[arr1[i] + arr2[i] + i, arr1[i] - arr2[i] + i, arr1[i] + arr2[i] - i, arr1[i] - arr2[i] - i] for i in range(len(arr1))]
        ans = 0
        for i in range(4):
            max_val = max(num[i] for num in nums)
            min_val = min(num[i] for num in nums)
            ans = max(ans, max_val - min_val)

        return ans
