from sortedcontainers import SortedSet

class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        n = len(nums) // 2
        total = sum(nums)
        goal = total / 2
        
        # generate a dictionary: length of subsequence -> all possible subsequence sums
        def generateSubSums(nums) -> dict:
            dp = defaultdict(SortedSet)
            dp[0].add(0)

            for num in nums:
                for l in range(len(nums), 0, -1):
                    dp[l].update(x + num for x in dp[l-1])

            return dp

        ans = inf
        first_half = generateSubSums(nums[::2])
        second_half = generateSubSums(nums[1::2])
        for l, first_subset in first_half.items():
            second_subset = second_half[n - l]
            for first_half_sum in first_subset:
                idx = second_subset.bisect_left(goal - first_half_sum)
                if idx < len(second_subset):
                    curr = first_half_sum + second_subset[idx]
                    ans = min(ans, abs(total - 2 * curr))
                if idx > 0:
                    curr = first_half_sum + second_subset[idx-1]
                    ans = min(ans, abs(total - 2 * curr))
    
        return ans
