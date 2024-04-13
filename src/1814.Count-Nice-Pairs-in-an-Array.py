class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        # nums[i] - rev(nums[i]) == nums[j] - rev(nums[j])

        # calculate num - rev(num) for some num, O(1), given num <= 10 ** 5
        def calTarget(num) -> int:
            return num - int(str(num)[::-1])

        ans = 0
        ht = defaultdict(int)
        for num in nums:
            target = calTarget(num)
            ans = (ans + ht[target]) % mod
            ht[target] += 1

        return ans
