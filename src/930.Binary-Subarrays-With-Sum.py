class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        lookup_table = Counter()
        lookup_table[0] = 1
        prefix_sum = 0
        ans = 0
        for num in nums:
            prefix_sum += num
            ans += lookup_table[prefix_sum - goal]
            lookup_table[prefix_sum] += 1

        return ans
